# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /tmp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3","app.py"]