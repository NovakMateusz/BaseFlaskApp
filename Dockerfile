FROM python:3.7.5-slim-buster
MAINTAINER Mateusz Nowak <novak.mateusz94@gmail.com>

ENV INSTALL_PATH /base_app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "base_app.app:create_app()"
