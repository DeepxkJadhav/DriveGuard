from sqlalchemy import Column, Integer, Float, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(JSON)  # {"lat": float, "lon": float}
    hazards = Column(JSON)   # [{"type": str, "confidence": float, "bbox": [xmin, ymin, xmax, ymax]}]
