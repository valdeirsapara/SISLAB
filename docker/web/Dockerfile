FROM github.com/valdeir027/docker/python:latest

COPY . /app/src/

WORKDIR /app/src

RUN mkdir -p /app/src/staticfiles_producao/ /app/src/log/

RUN python manage.py collectstatic --clear --noinput

EXPOSE 8000