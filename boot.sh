#!/bin/sh
source venv/bin/activate
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
done
[[ -z "$(PORT)" ]] && port=5000 || port="$(PORT)"
exec gunicorn --access-logfile - --error-logfile - simulador:app