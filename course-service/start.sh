#!/bin/bash
# Wait for DB
while ! python manage.py shell -c "import django; django.setup(); from django.db import connection; connection.ensure_connection()" 2>/dev/null; do
  echo "Waiting for database..."
  sleep 2
done
echo "Database ready, running migrations..."
python manage.py migrate
echo "Waiting for RabbitMQ..."
while ! timeout 1 bash -c 'cat < /dev/null > /dev/tcp/rabbitmq/5672'; do
  echo "Waiting for RabbitMQ..."
  sleep 2
done
echo "RabbitMQ ready, starting celery worker and beat..."
celery -A course_project worker --loglevel=info &
celery -A course_project beat --loglevel=info &
echo "Starting gunicorn server..."
gunicorn course_project.wsgi:application --bind 0.0.0.0:8000 --workers 3
