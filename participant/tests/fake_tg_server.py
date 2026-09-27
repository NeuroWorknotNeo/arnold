"""Поддельный Telegram как отдельный процесс (для e2e-проверки в Docker)."""

import argparse
import time

from tests.fake_telegram import FakeTelegram


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8080)
    args = ap.parse_args()
    FakeTelegram(host="0.0.0.0", port=args.port).start()
    print(f"fake telegram on :{args.port}", flush=True)
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    main()
