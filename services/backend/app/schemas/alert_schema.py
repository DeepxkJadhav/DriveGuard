from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class Hazard(BaseModel):
    type: str
    confidence: float
    bbox: List[int]

class AlertResponse(BaseModel):
    timestamp: datetime
    location: Dict[str, float]
    hazards: List[Hazard]

    class Config:
        orm_mode = True
