FROM python:3.11.0-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY app/ /app

WORKDIR /app

CMD ["python", "main.py"]
