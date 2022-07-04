# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /tmp/teste_flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3",".tmp/teste_flask/app.py"]
