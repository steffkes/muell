FROM python:3.9.1-alpine3.12

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
