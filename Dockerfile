FROM python:3.7

WORKDIR /app

RUN mkdir outputs

COPY . .

RUN pip install -r requirements.txt
