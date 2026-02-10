FROM python:3.13-alpine3.21

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
COPY src /app/
WORKDIR /app

CMD ["gunicorn","app:app"]
