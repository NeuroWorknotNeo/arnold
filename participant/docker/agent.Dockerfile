# Агент участника: Claude Code (по подписке владельца), цикл работы и инструменты доски.
# Токена Telegram-бота здесь нет: доска доступна только через сокет транспорта.
FROM node:22-bookworm-slim

ARG CLAUDE_CODE_VERSION=latest
ARG WITH_TEX=0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates curl git gh jq less procps ripgrep unzip \
        python3 python3-pip python3-venv \
        python3-numpy python3-scipy python3-sympy python3-mpmath python3-matplotlib python3-networkx \
    && if [ "$WITH_TEX" = "1" ]; then \
        apt-get install -y --no-install-recommends texlive-latex-base texlive-latex-recommended \
            texlive-latex-extra texlive-lang-cyrillic latexmk; \
       fi \
    && rm -rf /var/lib/apt/lists/*

# Claude Code ставится в системный каталог (вне тома с домашним каталогом),
# поэтому обновление = пересборка образа; самообновление отключено.
ENV NPM_CONFIG_PREFIX=/opt/npm-global PATH=/opt/npm-global/bin:$PATH
RUN npm install -g "@anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}" && npm cache clean --force \
    && claude --version

RUN groupadd -g 10002 agent && useradd -m -u 10002 -g 10002 -s /bin/bash agent \
    && mkdir -p /work /run/board && chown agent:agent /work && chmod 1777 /run/board

COPY board /opt/board/board
COPY docker/agent-entrypoint.sh /usr/local/bin/agent-entrypoint
RUN for tool in cli:board hook:board-hook runner:board-runner; do \
        printf '#!/bin/sh\nexec python3 -m board.%s "$@"\n' "${tool%%:*}" > "/usr/local/bin/${tool#*:}"; \
        chmod 755 "/usr/local/bin/${tool#*:}"; \
    done \
    && chmod 755 /usr/local/bin/agent-entrypoint

ENV PYTHONPATH=/opt/board PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    DISABLE_AUTOUPDATER=1 CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 \
    BOARD_SOCKET=/run/board/board.sock BOARD_INBOX=/work/inbox WORKDIR=/work/repo \
    MPLCONFIGDIR=/home/agent/.cache/matplotlib SHELL=/bin/bash

USER agent
WORKDIR /work
ENTRYPOINT ["agent-entrypoint"]
