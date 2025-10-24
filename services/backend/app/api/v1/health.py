from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def health_check():
    return {"status": "ok", "message": "DriveGuard backend is running"}
