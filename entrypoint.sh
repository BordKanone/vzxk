python manage.py makemigrations
python manage.py migrate
gunicorn config.wsgi:application --bind 0.0.0.0:8000
psql createuser bordkanone -W 5ed903dFERBS
psql createdb vzxk -O bordkanone
