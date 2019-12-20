FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install python3-dev -y

RUN mkdir /app
WORKDIR /app
COPY . .

# Устанавливаем зависимости проекта
RUN pip3 install -r requirements.txt

# Делаем файл запуска gunicorn исполняемым
RUN ["chmod", "+x", "/app/entrypoint.sh"]

# CMD команда будет запускаться при старте контейнера
CMD ["/app/entrypoint.sh"]
