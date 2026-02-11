LABEL org.opencontainers.image.authors="Hein Htet Zaw <h3inhtetzaw346@gmail.com>"
FROM python:3.13-alpine3.22

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
COPY src /app/
WORKDIR /app

CMD ["gunicorn","app:app"]
