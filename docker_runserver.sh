#!/usr/bin/env sh

echo "Run manage.py migrate"
python manage.py collectstatic --noinput
python manage.py migrate --noinput
echo "Run server"
PORT="${VARIABLE:=8000}"
exec ./manage.py rqworker --with-schedule & gunicorn news.wsgi -b 0.0.0.0:$PORT