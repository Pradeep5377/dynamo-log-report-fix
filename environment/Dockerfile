FROM python:3.11-slim

RUN pip install --no-cache-dir \
    pytest==8.4.1 \
    pytest-json-report==1.5.0

WORKDIR /app

COPY access.log /app/access.log