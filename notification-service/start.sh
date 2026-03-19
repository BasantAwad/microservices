#!/bin/bash
# Wait for DB
while ! python manage.py shell -c "import django; django.setup(); from django.db import connection; connection.ensure_connection()" 2>/dev/null; do
  echo "Waiting for database..."
  sleep 2
done
echo "Database ready, running migrations..."
python manage.py migrate
echo "Waiting for RabbitMQ..."
while ! nc -z rabbitmq 5672; do
  echo "Waiting for RabbitMQ..."
  sleep 2
done
echo "RabbitMQ ready, starting celery worker and beat..."
celery -A notification_project worker --loglevel=info &
celery -A notification_project beat --loglevel=info &
echo "Starting gunicorn server..."
gunicorn notification_project.wsgi:application --bind 0.0.0.0:8000 --workers 3
