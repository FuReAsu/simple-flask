FROM python:3.14-rc-alpine3.21

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir /app
COPY app /app/
WORKDIR /app

CMD ["gunicorn","app:app"]
