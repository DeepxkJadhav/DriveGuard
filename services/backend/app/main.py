from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import alerts, health

app = FastAPI(title="DriveGuard Backend API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(health.router, prefix="/api/v1/health", tags=["health"])
app.include_router(alerts.router, prefix="/api/v1/alerts", tags=["alerts"])

@app.on_event("startup")
async def startup_event():
    print("[INFO] DriveGuard backend starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    print("[INFO] DriveGuard backend shutting down...")
