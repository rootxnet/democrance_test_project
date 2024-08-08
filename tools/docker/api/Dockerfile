FROM python:3.12-bookworm
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

3COPY ./api/requirements.txt .

RUN apt update && apt upgrade -y && \
    pip install -r requirements.txt --upgrade
