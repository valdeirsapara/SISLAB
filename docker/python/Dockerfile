FROM python:3.13-slim


RUN apt-get update && apt-get install

RUN mkdir -p /app/src/

COPY requirements.txt /app/src/requirements.txt


RUN pip install --upgrade pip

RUN pip install -r /app/src/requirements.txt