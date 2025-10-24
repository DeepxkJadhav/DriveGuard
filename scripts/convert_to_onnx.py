from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "driveguard_custom_yolov8.pt"
EXPORT_DIR = Path(__file__).parent.parent / "onnx"

EXPORT_DIR.mkdir(exist_ok=True, parents=True)

# Load trained model
model = YOLO(MODEL_PATH)

# Export to ONNX
onnx_path = EXPORT_DIR / "driveguard.onnx"
model.export(format="onnx", imgsz=640)
print(f"✅ Model exported to ONNX: {onnx_path}")
