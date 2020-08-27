manage.py migrate
web: gunicorn project.wsgi:application --preload --workers 1
python manage.py collectstatic --noinput
