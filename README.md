```markdown
# DriveGuard

**Real-time road hazard detection for smarter, safer driving.**

DriveGuard is an end-to-end edge-to-cloud system that detects road hazards—like potholes, cracks, and obstacles—in real time using on-device AI, streams alerts via MQTT, and visualizes incidents through a responsive web dashboard. Built for deployment on fleet vehicles, municipal infrastructure, or personal dashcams.

---

## 🚦 Key Features

- **On-device inference**: Lightweight YOLOv8 model runs directly on edge hardware (Jetson, Raspberry Pi, etc.)
- **Low-latency alerting**: GPS-tagged hazard detections published over MQTT
- **Cloud backend**: FastAPI service ingests, stores, and serves alerts
- **Live dashboard**: Interactive map and alert feed (web + mobile-ready)
- **Model portability**: ONNX support for cross-platform deployment
- **Infrastructure-as-Code**: Terraform (AWS) + Kubernetes manifests included

---

## 📦 Project Structure

```
driveguard/
├── services/ Core components: edge, backend, frontend

├── models/ Trained YOLOv8 weights and ONNX exports

├── scripts/ Dataset prep, training, conversion utilities

├── deployment/ Kubernetes & Terraform configs

├── infra/ Mosquitto MQTT + Nginx configs

├── data/ Sample videos and annotations

└── docs/ Architecture, dataset spec, demo guide
```

---

## 🚀 Quick Start

1. **Clone & setup**
   ```bash
   git clone https://github.com/DeepxkJadhav/driveguard.git
   cd driveguard
   cp .env.example .env  # configure as needed
   ```

2. **Build and run locally**
   ```bash
   docker-compose up --build
   ```
   - Edge simulator → publishes mock alerts  
   - Backend → `http://localhost:8000`  
   - Frontend → `http://localhost:3000`

3. **Run a live demo**
   ```bash
   ./utilities/demo_runner.sh
   ```
   Processes `data/raw/sample_road_video.mp4` and visualizes detections.

---

## 🛠️ Development

- **Train your own model**  
  ```bash
  python scripts/train_yolo.py --data data/annotations/pothole_annotations.json
  ```

- **Convert to ONNX**  
  ```bash
  python scripts/convert_to_onnx.py
  ```

- **Run tests**  
  ```bash
  make test
  ```

---

## 🌐 Deployment

### Edge Device
Build and deploy the edge container:
```bash
docker build -t driveguard-edge -f services/edge_device/Dockerfile .
```

### Cloud (AWS + Kubernetes)
```bash
cd deployment/terraform
terraform apply  # provisions EKS, S3, etc.

kubectl apply -f ../k8s/
```

See `docs/deployment-guide.md` for full production setup.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

> **DriveGuard**: Because the road shouldn’t surprise you.  
> Built with precision. Deployed with purpose.
> 
```
