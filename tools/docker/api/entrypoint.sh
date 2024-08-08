#!/usr/bin/env sh

python manage.py migrate
python manage.py collectstatic --noinput

# Use gunicorn for staging and production
# gunicorn api.wsgi:application --bind=0.0.0.0:8000 --workers=4 --timeout=3600 --reload --access-logfile -

# Use Django's built-in development server for local development
python manage.py runserver 0.0.0.0:8000