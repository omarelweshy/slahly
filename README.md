# Welcome to slahly

For DATABASE you can comment MySQL or reconfig it or comment out SQLite3 Database.

For Stripe and email you can will find constractions on `settings.py`.

## How to run the project

First you should install requirements via `pip install -r requirements.txt && python manage.py migrate` then you can start server via `python manage.py runserver` and finally navigate to `http://127.0.0.1:8000/`

## Start with Docker

run `docker-compose build` then `docker-compose up`
