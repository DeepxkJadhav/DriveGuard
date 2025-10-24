from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.core import models
from app.schemas.alert_schema import AlertResponse

router = APIRouter()

@router.get("/", response_model=list[AlertResponse])
def get_alerts(db: Session = Depends(get_db)):
    alerts = db.query(models.Alert).order_by(models.Alert.timestamp.desc()).all()
    return alerts

@router.get("/latest", response_model=AlertResponse)
def get_latest_alert(db: Session = Depends(get_db)):
    alert = db.query(models.Alert).order_by(models.Alert.timestamp.desc()).first()
    if not alert:
        raise HTTPException(status_code=404, detail="No alerts found")
    return alert
