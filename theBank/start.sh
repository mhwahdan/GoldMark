conda activate theBank

gunicorn3 --bind 0.0.0.0:8000 theBank.wsgi:application
