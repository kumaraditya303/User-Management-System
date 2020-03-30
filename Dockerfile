FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN pip install -r /code/requirements.txt
RUN pytest
RUN adduser -D user
USER user

EXPOSE 5000
