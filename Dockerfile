FROM python:3.8

WORKDIR /opt/rest_fastapi

COPY requirements.txt ./
RUN pip install -r requirements.txt