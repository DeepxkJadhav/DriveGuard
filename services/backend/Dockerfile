FROM python:3.11-slim

WORKDIR /app

COPY app/ ./app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV MQTT_BROKER_HOST=driveguard-mqtt
ENV MQTT_BROKER_PORT=1883
ENV MQTT_TOPIC=driveguard/alerts
ENV DATABASE_URL=sqlite:///./driveguard.db

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
