# Транспорт участника: единственный держатель токена Telegram-бота.
FROM python:3.12-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -g 10001 board && useradd -m -u 10001 -g 10001 -s /usr/sbin/nologin board \
    && mkdir -p /data /run/board && chown board:board /data && chmod 1777 /run/board

COPY board /opt/board/board
ENV PYTHONPATH=/opt/board PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 HOME=/home/board

USER board
HEALTHCHECK --interval=60s --timeout=5s --start-period=90s --retries=3 \
  CMD python3 -c "import sys,time; sys.exit(0 if time.time()-int(open('/data/heartbeat').read())<120 else 1)"
ENTRYPOINT ["python3", "-m", "board.transport"]
