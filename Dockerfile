FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app/

CMD python manage.py runserver 0.0.0.0:8000