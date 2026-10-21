# Главный агент на сервере: запуск и управление

Главный агент — интерактивная сессия Claude Code в папке `/home/claudeagent/arnold` (ссылка
`/root/arnold`). Он работает под пользователем `claudeagent` внутри tmux, а запускает его служба
systemd `arnold-agent`. С агентом говорят из приложения Claude (телефон, компьютер,
claude.ai/code) через Remote Control. Ваш компьютер для этого не нужен.

- Модель — Opus 5.5 с effort max.
- Режим — без подтверждения действий (`bypassPermissions`), но без прав root.
- Рабочие агенты — подагенты из `.claude/agents/`, их запускает сам главный агент.
- Роль, правила и порядок работы описаны в [CLAUDE.md](../CLAUDE.md).

## Как это устроено

```
 приложение Claude ──Remote Control──► tmux «arnold» (claudeagent)
                                         └─ ops/arnold-agent.sh — перезапускает claude:
                                              claude --remote-control --model claude-opus-5-5 --effort max
                                                 ├─ пульс раз в 30 мин (CronCreate): продолжать работу
                                                 └─ подагенты: prover, reviewer, literature, numerics
 служба systemd arnold-agent ──► поднимает tmux при загрузке сервера
 GitHub NeuroWorknotNeo/arnold ◄── коммиты главного агента (план, журнал, заметки, результаты)
```

Если Claude Code завершится (сбой, обновление, перезагрузка сервера), скрипт через 30 секунд
запустит его снова с `--continue`. Разговор продолжится, а агент получит сообщение «[перезапуск]»,
проверит пульс и продолжит работу.

## Первый запуск (один раз, под root)

1. Обновите клон:
   ```bash
   sudo -iu claudeagent git -C ~/arnold pull
   ```
2. Установите службу и всё нужное: tmux, Python-окружение для расчётов, настройки.
   ```bash
   bash /root/arnold/ops/install.sh
   ```
   В конце скрипт напишет «Готово» и следующие шаги. Если он предупредит про вход в Claude или
   GitHub, выполните названную им команду и запустите скрипт ещё раз.
3. Запустите агента и откройте его терминал:
   ```bash
   systemctl start arnold-agent
   sudo -iu claudeagent tmux attach -t arnold
   ```
   Claude Code задаст несколько вопросов, ответьте на них:
   - доверять папке — да;
   - включить Remote Control — да;
   - режим без подтверждений (bypass permissions) — принять.

   После этого агент начнёт работу. Уведомления на телефон включаются там же: наберите `/config`
   и включите **Push when Claude decides** и **Push when actions required**. Выйти из терминала, не
   останавливая агента: **Ctrl+B, затем D**.
4. В приложении Claude откройте сессию **«Арнольд — главный»** и пишите в неё.

## Управление (под root)

| Что | Команда |
|---|---|
| Состояние службы | `systemctl status arnold-agent` |
| Посмотреть терминал агента | `sudo -iu claudeagent tmux attach -t arnold` (выйти: Ctrl+B, затем D) |
| Перезапустить (разговор продолжится) | `systemctl restart arnold-agent` |
| Остановить | `systemctl stop arnold-agent` |
| Журнал перезапусков | `cat /home/claudeagent/.arnold-agent/restarts.log` |
| Обновить Claude Code | `sudo -iu claudeagent claude update && systemctl restart arnold-agent` |
| Войти в Claude заново | `sudo -iu claudeagent claude auth login` |

Поставить работу на паузу и снять её можно словами в самой сессии: «пауза» и «продолжай».

## Если что-то не так

- **Сессии нет в приложении.** Откройте терминал агента. Если там ошибка входа, выполните
  `sudo -iu claudeagent claude auth login`, затем `systemctl restart arnold-agent`. После сжатия
  контекста Remote Control иногда заводит новую сессию с тем же именем: ищите самую свежую
  «Арнольд — главный».
- **Агент молчит.** Возможно, кончился лимит подписки: работа продолжится после сброса. Квота
  общая: её тратят и агенты, и ваши собственные чаты с Claude.
- **Ошибка `does not support this model`.** Обновите Claude Code (команда выше).
- **Начать с чистого листа** (новый разговор; агент восстановит контекст по файлам плана и
  журнала):
  ```bash
  systemctl stop arnold-agent
  rm /home/claudeagent/.arnold-agent/has-session
  systemctl start arnold-agent
  ```

Не запускайте вручную `claude` в папке `~/arnold` под `claudeagent`, пока работает служба: при
перезапуске `--continue` может подхватить ваш разговор вместо разговора агента.
