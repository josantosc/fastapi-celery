FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc libcurl4-openssl-dev libssl-dev

COPY ../app/requirements.txt /app

RUN pip install -r requirements.txt
RUN apt autoremove -y