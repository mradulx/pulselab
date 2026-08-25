from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="PulseLab API",
    version="0.1.0",
    description="Real-time IoT telemetry API for PulseLab.",
)


class Telemetry(BaseModel):
    device_id: str = Field(min_length=1, max_length=64)
    temperature_c: float | None = None
    humidity_pct: float | None = Field(default=None, ge=0, le=100)
    light_lux: float | None = Field(default=None, ge=0)
    voltage_v: float | None = Field(default=None, ge=0)
    recorded_at: datetime | None = None


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/")
def root() -> dict[str, str]:
    return {"name": "PulseLab API", "version": "0.1.0"}


@app.post("/api/v1/telemetry", status_code=201)
def ingest_telemetry(payload: Telemetry) -> dict:
    timestamp = payload.recorded_at or datetime.now(timezone.utc)
    return {
        "accepted": True,
        "device_id": payload.device_id,
        "recorded_at": timestamp.isoformat(),
        "telemetry": payload.model_dump(exclude={"recorded_at"}),
    }
