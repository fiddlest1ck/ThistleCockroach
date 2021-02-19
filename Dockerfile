FROM python:3.9
RUN apt update -y

RUN mkdir app
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt

COPY . /app

EXPOSE 8000
WORKDIR /app
ENTRYPOINT ["/app/docker-entrypoint.sh"]
