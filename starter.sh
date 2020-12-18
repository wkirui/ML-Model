#!/bin/bash
exec gunicorn --config gunicorn_config.py wsgi:app

# app="docker.naimodel"
# docker build -t ${app} .
# docker run -d -p 56733:80 \
#     --name=${app} \
#     -v /app/ ${app}