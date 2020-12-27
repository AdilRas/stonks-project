#!/bin/sh

set -e

python manage.py collectstatic --noinput

uWSGI --socket :8000 --master --enable-threads --module app.wsgi
