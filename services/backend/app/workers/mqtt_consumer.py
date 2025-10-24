import json
import os
import paho.mqtt.client as mqtt
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from app.core.models import Alert
from datetime import datetime

BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "localhost")
BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 1883))
TOPIC = os.getenv("MQTT_TOPIC", "driveguard/alerts")

def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    db: Session = SessionLocal()
    try:
        payload = json.loads(msg.payload)
        alert = Alert(
            timestamp=datetime.fromtimestamp(payload["timestamp"]),
            location=payload["location"],
            hazards=payload["hazards"]
        )
        db.add(alert)
        db.commit()
        print(f"[MQTT] Alert saved: {payload}")
    except Exception as e:
        print(f"[MQTT] Failed to process message: {e}")
    finally:
        db.close()

client = mqtt.Client("DriveGuardBackend")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_HOST, BROKER_PORT, 60)
client.loop_forever()
