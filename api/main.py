import os
from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, select
import motor.motor_asyncio
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Data-Continuum Unified Extraction API")

Instrumentator().instrument(app).expose(app)

POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/continuum")
MONGO_URL = os.getenv("MONGO_URL", "mongodb://admin:admin@localhost:27017/")

# Postgres setup
engine = create_async_engine(POSTGRES_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String)
    customer_email = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Mongo setup
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client['continuum']
telemetry_col = db['telemetry']

class UnifiedState(BaseModel):
    shipment_id: int
    customer_name: str
    status: str
    latitude: Optional[float]
    longitude: Optional[float]
    engine_temp: Optional[float]
    fuel_level: Optional[float]
    telemetry_timestamp: Optional[datetime]

@app.get("/shipments/{shipment_id}/unified", response_model=UnifiedState)
async def get_unified_shipment_state(shipment_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Shipment).where(Shipment.id == shipment_id))
        shipment = result.scalars().first()
        
        if not shipment:
            raise HTTPException(status_code=404, detail="Shipment not found")

    telemetry = await telemetry_col.find_one({"shipment_id": shipment_id}, sort=[("timestamp", -1)])
    
    return UnifiedState(
        shipment_id=shipment.id,
        customer_name=shipment.customer_name,
        status=shipment.status,
        latitude=telemetry["latitude"] if telemetry else None,
        longitude=telemetry["longitude"] if telemetry else None,
        engine_temp=telemetry["engine_temp"] if telemetry else None,
        fuel_level=telemetry["fuel_level"] if telemetry else None,
        telemetry_timestamp=telemetry["timestamp"] if telemetry else None
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Serve UI static files
ui_path = os.path.join(os.path.dirname(__file__), "ui")
if os.path.exists(ui_path):
    app.mount("/", StaticFiles(directory=ui_path, html=True), name="ui")
