FROM python:3

MAINTAINER Fernando Mariano <fernando.mar16@gmail.com>

RUN pip install tweepy \
    pymongo

COPY ./ /app

WORKDIR /app

CMD ['python3', 'app.py']