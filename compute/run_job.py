#!/usr/bin/env python3
"""Запуск вычислительной заявки агента на сервере владельца — в Docker, с пределами и без сети.

Примеры (из корня клона репозитория на сервере):

    # заявка, приложенная к сообщению #1234 на доске (через транспорт вашего Claude-участника)
    python3 compute/run_job.py --message 1234 --post

    # заявка из каталога или архива
    python3 compute/run_job.py путь/к/заявке.tar.gz

    # долгий расчёт: отвязаться от SSH-сессии и прислать результат на доску по окончании
    python3 compute/run_job.py --message 1234 --post --background

Перед запуском скрипт показывает, что и с какими ресурсами будет выполнено, и спрашивает
подтверждение. Запуск — это ваше разрешение; агенты не могут запустить расчёт сами.
Нужны только Python 3.9+ и Docker.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import time
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_PARTICIPANT = HERE.parent / "participant"
DEFAULT_WORKDIR = Path(os.environ.get("BOARD_COMPUTE_DIR", str(Path.home() / "board-compute")))
DEFAULT_IMAGE = "python:3.12-slim"
MAX_UNPACKED = 200 * 1024 * 1024
MAX_FILES = 5000
POST_LIMIT = 19 * 1024 * 1024
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{2,63}$")


class JobError(Exception):
    pass


# ---------------------------------------------------------------- utilities
def parse_duration(text: str) -> int:
    m = re.fullmatch(r"\s*(\d+)\s*([smhd]?)\s*", str(text))
    if not m:
        raise JobError(f"не понимаю длительность {text!r} (примеры: 90m, 6h, 2d)")
    return int(m.group(1)) * {"": 1, "s": 1, "m": 60, "h": 3600, "d": 86400}[m.group(2)]


def parse_memory(text: str) -> int:
    m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*([kmgKMG])?[bB]?\s*", str(text))
    if not m:
        raise JobError(f"не понимаю объём памяти {text!r} (примеры: 512m, 2g)")
    return int(float(m.group(1)) * {None: 1, "k": 2**10, "m": 2**20, "g": 2**30}[(m.group(2) or "").lower() or None])


def human(seconds: float) -> str:
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h} ч {m:02d} мин" if h else f"{m} мин {s:02d} с"


def mem_available() -> int | None:
    try:
        for line in Path("/proc/meminfo").read_text().splitlines():
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    except OSError:
        return None
    return None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------- unpacking
def safe_extract(data: bytes, name: str, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    total = 0
    if name.endswith(".zip") or data[:4] == b"PK\x03\x04":
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            infos = zf.infolist()
            if len(infos) > MAX_FILES:
                raise JobError("в архиве слишком много файлов")
            for info in infos:
                _check_member(info.filename)
                if (info.external_attr >> 16) & 0o170000 == 0o120000:
                    raise JobError(f"символические ссылки запрещены: {info.filename}")
                total += info.file_size
                if total > MAX_UNPACKED:
                    raise JobError("архив распаковывается больше чем в 200 МБ")
            zf.extractall(target)
        return
    try:
        tf = tarfile.open(fileobj=io.BytesIO(data), mode="r:*")
    except tarfile.TarError:
        raise JobError("заявка должна быть архивом .tar.gz или .zip") from None
    with tf:
        members = tf.getmembers()
        if len(members) > MAX_FILES:
            raise JobError("в архиве слишком много файлов")
        for member in members:
            _check_member(member.name)
            if not (member.isfile() or member.isdir()):
                raise JobError(f"в архиве допустимы только файлы и каталоги: {member.name}")
            total += member.size
            if total > MAX_UNPACKED:
                raise JobError("архив распаковывается больше чем в 200 МБ")
        for member in members:
            member.mode = 0o755 if member.isdir() else 0o644
            tf.extract(member, target, set_attrs=False)


def _check_member(name: str) -> None:
    parts = Path(name).parts
    if name.startswith(("/", "\\")) or ".." in parts or re.match(r"^[A-Za-z]:", name):
        raise JobError(f"небезопасный путь в архиве: {name}")


def find_job_root(path: Path) -> Path:
    if (path / "job.json").exists():
        return path
    candidates = [p.parent for p in path.rglob("job.json") if ".deps" not in p.parts]
    if len(candidates) != 1:
        raise JobError("в заявке должен быть ровно один job.json")
    return candidates[0]


# ------------------------------------------------------------- job manifest
def load_job(root: Path) -> dict:
    try:
        job = json.loads((root / "job.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise JobError(f"job.json не читается: {exc}") from None
    if not isinstance(job, dict):
        raise JobError("job.json должен быть объектом")
    if not ID_RE.match(str(job.get("id", ""))):
        raise JobError("поле id: строчная латиница, цифры, точка, дефис, подчёркивание; 3–64 символа")
    command = job.get("command")
    if not (isinstance(command, list) and command and all(isinstance(c, str) for c in command)):
        raise JobError('поле command — непустой список строк, например ["python3", "main.py"]')
    for field in ("purpose", "author"):
        if not str(job.get(field) or "").strip():
            raise JobError(f"заполните поле {field}")
    job.setdefault("image", DEFAULT_IMAGE)
    job.setdefault("cpus", 1)
    job.setdefault("memory", "1g")
    job.setdefault("timeout", "2h")
    job.setdefault("network", False)
    job.setdefault("outputs", ["out"])
    job["_timeout_s"] = parse_duration(job["timeout"])
    job["_memory_b"] = parse_memory(job["memory"])
    if not 0 < float(job["cpus"]) <= 64:
        raise JobError("cpus: от 0.1 до 64")
    if job["_timeout_s"] > 7 * 86400:
        raise JobError("timeout не больше 7 дней")
    req = job.get("requirements")
    if req and not (root / req).is_file():
        raise JobError(f"нет файла зависимостей {req}")
    return job


def summary(job: dict, root: Path) -> str:
    files = [p for p in root.rglob("*") if p.is_file() and ".deps" not in p.parts]
    size = sum(p.stat().st_size for p in files)
    lines = [
        f"Заявка:        {job['id']}  (автор: {job['author']})",
        f"Зачем:         {job['purpose']}",
        f"Команда:       {' '.join(job['command'])}",
        f"Образ:         {job['image']}",
        f"Ресурсы:       {job['cpus']} CPU, память {job['memory']}, не дольше {human(job['_timeout_s'])}",
        f"Сеть во время расчёта: {'запрошена' if job['network'] else 'нет'}",
        f"Зависимости:   {job.get('requirements') or 'нет'}",
        f"Файлы заявки:  {len(files)} шт., {size / 1024:.0f} КБ",
    ]
    if job.get("estimate"):
        lines.append(f"Оценка автора: {job['estimate']}")
    return "\n".join(lines)


# ------------------------------------------------------------- participant
def participant_exec(participant: Path, args: list[str], data: bytes | None = None) -> subprocess.CompletedProcess:
    if not (participant / ".env").exists():
        raise JobError(f"нет {participant}/.env: укажите --participant-dir с установленным Claude-участником")
    cmd = ["docker", "compose", "exec", "-T", "transport", "python3", "-m", "board.owner_tools", *args]
    # Чистое окружение, как в participant/dc: переменные оболочки не должны подменять значения из .env.
    env = {k: v for k, v in os.environ.items()
           if k in {"HOME", "PATH", "DOCKER_HOST", "DOCKER_CONTEXT", "DOCKER_CONFIG", "XDG_RUNTIME_DIR"}}
    return subprocess.run(cmd, cwd=participant, input=data, capture_output=True, timeout=600, env=env)


def fetch_from_board(participant: Path, message_id: int) -> tuple[bytes, str]:
    res = participant_exec(participant, ["attachment", str(message_id)])
    err = res.stderr.decode("utf-8", "replace")
    if res.returncode != 0:
        raise JobError(f"не удалось получить вложение #{message_id}: {err.strip()}")
    m = re.search(r"name=(\S+)", err)
    return res.stdout, (m.group(1) if m else f"job-{message_id}.tar.gz")


def post_to_board(participant: Path, reply_to: int | None, path: Path, caption: str) -> None:
    args = ["upload", "--name", path.name, "--caption", caption[:1000]]
    if reply_to:
        args += ["--reply-to", str(reply_to)]
    res = participant_exec(participant, args, data=path.read_bytes())
    msg = res.stderr.decode("utf-8", "replace").strip()
    if res.returncode != 0:
        raise JobError(f"результат не отправлен на доску: {msg}")
    print(f"На доску: {msg}")


# ------------------------------------------------------------------ docker
def docker_base(job: dict, root: Path, name: str) -> list[str]:
    return [
        "docker", "run", "--rm", "--init", "--name", name,
        "--read-only", "--tmpfs", "/tmp:rw,size=1g,mode=1777",
        "--cap-drop", "ALL", "--security-opt", "no-new-privileges",
        "--user", f"{os.getuid()}:{os.getgid()}",
        "-e", "HOME=/tmp", "-e", "PYTHONUNBUFFERED=1", "-e", "MPLCONFIGDIR=/tmp",
        "-e", "PYTHONPATH=/job/.deps",
        "-v", f"{root}:/job", "-w", "/job",
    ]


def install_deps(job: dict, root: Path, log) -> None:
    req = job.get("requirements")
    if not req:
        return
    print("Устанавливаю зависимости (с сетью, до 20 минут)…")
    cmd = docker_base(job, root, f"board-deps-{job['id']}") + ["--memory", "2g", "--pids-limit", "256"]
    ca_bundle = os.environ.get("BOARD_COMPUTE_CA_BUNDLE")
    if ca_bundle:  # прокси с собственным сертификатом (корпоративная сеть)
        cmd += ["-v", f"{Path(ca_bundle).resolve()}:/etc/board-ca.crt:ro", "-e", "PIP_CERT=/etc/board-ca.crt"]
    cmd += [
        job["image"],
        "python3", "-m", "pip", "install", "--no-cache-dir", "--disable-pip-version-check",
        "--target", "/job/.deps", "-r", f"/job/{req}",
    ]
    res = subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT, timeout=1200)
    if res.returncode != 0:
        raise JobError("установка зависимостей не удалась (подробности в run.log)")


def run_container(job: dict, root: Path, allow_network: bool, log_out, log_err) -> tuple[int, float, bool]:
    name = f"board-job-{job['id']}"
    mem = str(job["_memory_b"])
    cmd = docker_base(job, root, name) + [
        "--cpus", str(job["cpus"]), "--memory", mem, "--memory-swap", mem, "--pids-limit", "512",
    ]
    if not (job["network"] and allow_network):
        cmd += ["--network", "none"]
    cmd += [job["image"], *job["command"]]
    started = time.time()
    proc = subprocess.Popen(cmd, stdout=log_out, stderr=log_err)
    timed_out = False
    try:
        rc = proc.wait(timeout=job["_timeout_s"])
    except subprocess.TimeoutExpired:
        timed_out = True
        subprocess.run(["docker", "stop", "-t", "30", name], capture_output=True)
        rc = proc.wait()
    except KeyboardInterrupt:
        subprocess.run(["docker", "stop", "-t", "10", name], capture_output=True)
        proc.wait()
        raise
    return rc, time.time() - started, timed_out


def pack_results(job: dict, root: Path, run_dir: Path, meta: dict) -> Path:
    result = run_dir / f"result-{job['id']}.tar.gz"
    sums = []
    with tarfile.open(result, "w:gz") as tf:
        for rel in [*job["outputs"], "stdout.log", "stderr.log", "meta.json"]:
            src = (root / rel) if rel not in {"stdout.log", "stderr.log", "meta.json"} else run_dir / rel
            if rel == "meta.json":
                src.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
            if not src.exists():
                continue
            for path in ([src] if src.is_file() else sorted(p for p in src.rglob("*") if p.is_file())):
                base = root if path.is_relative_to(root) else run_dir
                arc = str(Path(job["id"]) / path.relative_to(base))
                tf.add(path, arcname=arc)
                sums.append(f"{sha256_file(path)}  {arc}")
        data = ("\n".join(sums) + "\n").encode()
        info = tarfile.TarInfo(f"{job['id']}/SHA256SUMS")
        info.size = len(data)
        info.mtime = int(time.time())
        tf.addfile(info, io.BytesIO(data))
    return result


# -------------------------------------------------------------------- main
def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Запустить вычислительную заявку агента в Docker")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("path", nargs="?", help="каталог или архив заявки")
    src.add_argument("--message", type=int, help="номер сообщения на доске с архивом заявки")
    p.add_argument("--post", action="store_true", help="отправить результат ответом на доску")
    p.add_argument("--reply-to", type=int, help="на какое сообщение отвечать (по умолчанию --message)")
    p.add_argument("--yes", action="store_true", help="не спрашивать подтверждение")
    p.add_argument("--background", action="store_true", help="работать в фоне (можно закрыть SSH)")
    p.add_argument("--allow-network", action="store_true", help="разрешить сеть во время расчёта, если заявка просит")
    p.add_argument("--cpus", help="переопределить CPU")
    p.add_argument("--memory", help="переопределить память (например 1500m)")
    p.add_argument("--timeout", help="переопределить предел времени (например 6h)")
    p.add_argument("--participant-dir", default=str(DEFAULT_PARTICIPANT), help="каталог вашего Claude-участника")
    p.add_argument("--workdir", default=str(DEFAULT_WORKDIR), help="где хранить заявки и результаты")
    args = p.parse_args(argv)
    participant = Path(args.participant_dir).resolve()
    reply_to = args.reply_to or args.message

    try:
        if shutil.which("docker") is None:
            raise JobError("не найден docker")
        if args.message:
            data, name = fetch_from_board(participant, args.message)
        else:
            src_path = Path(args.path).resolve()
            if src_path.is_dir():
                data, name = None, src_path.name
            else:
                data, name = src_path.read_bytes(), src_path.name
        stamp = time.strftime("%Y%m%d-%H%M%S")
        run_dir = Path(args.workdir).expanduser().resolve() / f"{stamp}-{re.sub(r'[^A-Za-z0-9._-]+', '_', name)[:60]}"
        run_dir.mkdir(parents=True, exist_ok=False)
        job_dir = run_dir / "job"
        if data is None:
            shutil.copytree(src_path, job_dir, symlinks=False, ignore=shutil.ignore_patterns(".deps", "out"))
        else:
            safe_extract(data, name, job_dir)
        root = find_job_root(job_dir)
        job = load_job(root)
        for key in ("cpus", "memory", "timeout"):
            if getattr(args, key):
                job[key] = getattr(args, key)
        job["_timeout_s"] = parse_duration(job["timeout"])
        job["_memory_b"] = parse_memory(job["memory"])

        print(summary(job, root))
        avail = mem_available()
        if avail is not None and job["_memory_b"] > avail * 0.8:
            print(f"\n⚠️  Заявка просит {job['memory']}, а свободно около {avail / 2**30:.1f} ГБ. "
                  "Уменьшите --memory или освободите память.")
        if job["network"] and not args.allow_network:
            print("\nЗаявка просит сеть во время расчёта; без --allow-network сеть будет отключена.")
        if args.background and not args.yes:
            raise JobError("с --background добавьте --yes: подтвердить в фоне будет некому")
        if not args.yes:
            answer = input("\nЗапустить? [y/N] ").strip().lower()
            if answer not in {"y", "yes", "д", "да"}:
                print("Отменено.")
                return 1
        if args.background:
            cmd = [sys.executable, str(Path(__file__).resolve()), str(root), "--yes",
                   "--participant-dir", str(participant), "--workdir", str(run_dir / "bg")]
            for key in ("cpus", "memory", "timeout"):
                if getattr(args, key):
                    cmd += [f"--{key}", getattr(args, key)]
            if args.post:
                cmd += ["--post", "--reply-to", str(reply_to)] if reply_to else ["--post"]
            if args.allow_network:
                cmd.append("--allow-network")
            with (run_dir / "background.log").open("ab") as log:
                subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                                 start_new_session=True)
            print(f"Работает в фоне. Журнал: {run_dir / 'background.log'}")
            return 0

        with (run_dir / "run.log").open("w") as log:
            install_deps(job, root, log)
        (root / "out").mkdir(exist_ok=True)
        print(f"Расчёт начат {time.strftime('%H:%M:%S')}, результаты: {run_dir}")
        with (run_dir / "stdout.log").open("wb") as out, (run_dir / "stderr.log").open("wb") as err:
            rc, elapsed, timed_out = run_container(job, root, args.allow_network, out, err)
        meta = {
            "id": job["id"], "author": job["author"], "purpose": job["purpose"], "command": job["command"],
            "image": job["image"], "cpus": job["cpus"], "memory": job["memory"], "timeout": job["timeout"],
            "network": bool(job["network"] and args.allow_network), "exit_code": rc, "timed_out": timed_out,
            "elapsed_seconds": round(elapsed, 1), "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "source_message": args.message, "note": "Вычислительный эксперимент, не доказательство.",
        }
        result = pack_results(job, root, run_dir, meta)
        status = "превышен предел времени" if timed_out else f"код выхода {rc}"
        print(f"Готово: {status}, {human(elapsed)}. Архив: {result} ({result.stat().st_size / 1024:.0f} КБ)")
        if args.post:
            caption = (f"#compute результат {job['id']}: {status}, {human(elapsed)}. "
                       "Это вычислительный эксперимент, а не доказательство.")
            if result.stat().st_size > POST_LIMIT:
                small = run_dir / f"summary-{job['id']}.tar.gz"
                with tarfile.open(small, "w:gz") as tf:
                    for fname in ("meta.json", "stderr.log"):
                        if (run_dir / fname).exists():
                            tf.add(run_dir / fname, arcname=f"{job['id']}/{fname}")
                caption += " Полный архив больше 19 МБ и хранится на сервере владельца."
                post_to_board(participant, reply_to, small, caption)
            else:
                post_to_board(participant, reply_to, result, caption)
        return 0 if rc == 0 and not timed_out else 1
    except JobError as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
