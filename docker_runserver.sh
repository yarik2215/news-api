#!/usr/bin/env sh

echo "Run manage.py migrate"
python manage.py collectstatic --noinput
python manage.py migrate --noinput
echo "Run server"
exec  gunicorn news.wsgi -b 0.0.0.0:$PORT