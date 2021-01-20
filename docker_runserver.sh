#!/usr/bin/env sh

echo "Run manage.py migrate"
python /code/manage.py migrate --noinput
echo "Run server"
exec  python -Wd manage.py runserver 0.0.0.0:9000