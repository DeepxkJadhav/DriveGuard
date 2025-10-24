import cv2
import torch
import time
import os
from mqtt_publisher import publish_alert
from gps_reader import get_current_location

# Load the YOLOv8 model (ONNX or PyTorch)
MODEL_PATH = os.getenv("MODEL_PATH", "models/yolov8/driveguard_custom_yolov8.pt")
CONF_THRESHOLD = float(os.getenv("CONF_THRESHOLD", 0.4))

print(f"[INFO] Loading YOLOv8 model from {MODEL_PATH}")
model = torch.hub.load('ultralytics/yolov8', 'custom', path=MODEL_PATH)

def process_frame(frame):
    """Run detection on a single frame and publish alert if hazard detected."""
    results = model(frame)
    detections = results.pandas().xyxy[0]  # pandas DataFrame
    hazards = []

    for _, row in detections.iterrows():
        if row['confidence'] >= CONF_THRESHOLD:
            hazards.append({
                "type": row['name'],
                "confidence": float(row['confidence']),
                "bbox": [int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])]
            })
    
    if hazards:
        location = get_current_location()
        alert = {
            "timestamp": int(time.time()),
            "location": location,
            "hazards": hazards
        }
        publish_alert(alert)

def run_video(video_source=0):
    """Process video from camera or file."""
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        raise RuntimeError(f"[ERROR] Unable to open video source: {video_source}")
    
    print("[INFO] Starting video processing...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        process_frame(frame)

        # Optional: display the frame for debugging
        cv2.imshow("DriveGuard Edge", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_src = os.getenv("VIDEO_SOURCE", 0)
    run_video(video_src)
