web: gunicorn frontida_backend.wsgi:application --preload --workers 1
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
