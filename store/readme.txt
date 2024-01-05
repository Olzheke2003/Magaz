ДЛЯ ЗАПУСКА CELERY:
установить eventlet
и в терминале celery -A store worker --loglevel=info -P eventlet

REDIS:
cd C:\Program Files\Redis
запускаем redis-cli.exe;
выключаем сервер командой shutdown;
выходим командой exit.
потом redis-server