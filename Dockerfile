FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app

ENV STATIC_URL /app/static
ENV STATIC_PATH /app/static

ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD . /app
EXPOSE 5000
RUN chmod +x starter.sh
ENTRYPOINT ["sh", "starter.sh"]