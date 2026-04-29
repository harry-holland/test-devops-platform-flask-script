FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt && pip install influxdb

COPY . .

EXPOSE 7777

CMD ["python", "main.py"]
