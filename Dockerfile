FROM python:3.6-alpine

RUN adduser -D ruleta

WORKDIR /home/ruleta

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY simulador.py ./
COPY config.py ./
COPY boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP simulador.py

RUN chown -R ruleta:ruleta ./
USER ruleta

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]