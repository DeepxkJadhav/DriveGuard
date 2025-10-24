import json
import os
import paho.mqtt.client as mqtt

BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "localhost")
BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 1883))
TOPIC = os.getenv("MQTT_TOPIC", "driveguard/alerts")

client = mqtt.Client("DriveGuardEdge")
client.connect(BROKER_HOST, BROKER_PORT, 60)
client.loop_start()

def publish_alert(alert: dict):
    """Publish alert dictionary as JSON to MQTT broker."""
    payload = json.dumps(alert)
    result = client.publish(TOPIC, payload)
    if result.rc == 0:
        print(f"[MQTT] Alert published: {payload}")
    else:
        print(f"[MQTT] Failed to publish alert: {payload}")
