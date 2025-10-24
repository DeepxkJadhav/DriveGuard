import yaml
from ultralytics import YOLO
from pathlib import Path

# Config paths
CONFIG_DIR = Path(__file__).parent / "configs"
TRAIN_CONFIG = CONFIG_DIR / "yolov8_train.yaml"

# Load YAML training config
with open(TRAIN_CONFIG) as f:
    cfg = yaml.safe_load(f)

# Initialize model
model = YOLO(cfg['model_weights'])

# Train the model
model.train(
    data=cfg['data'],          # path to dataset YAML/json
    epochs=cfg['epochs'],
    batch=cfg['batch_size'],
    imgsz=cfg['img_size'],
    optimizer=cfg['optimizer'],
    project=cfg['save_dir'],
    name=cfg['experiment_name'],
    device=cfg.get('device', '0')
)

# Save trained weights
model.save(Path(cfg['save_dir']) / f"{cfg['experiment_name']}.pt")
print("✅ Training complete and model saved!")
