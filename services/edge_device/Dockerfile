# Base image with Python & OpenCV
FROM python:3.11-slim

WORKDIR /app

# Copy edge app
COPY app/ ./app
COPY configs/device_config.yml ./configs/device_config.yml
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables from config
ENV MODEL_PATH=./models/yolov8/driveguard_custom_yolov8.pt
ENV VIDEO_SOURCE=0
ENV CONF_THRESHOLD=0.4
ENV MQTT_BROKER_HOST=driveguard-mqtt
ENV MQTT_BROKER_PORT=1883
ENV MQTT_TOPIC=driveguard/alerts

CMD ["python", "app/edge_detector.py"]
