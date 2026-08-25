from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ingest_telemetry() -> None:
    response = client.post(
        "/api/v1/telemetry",
        json={
            "device_id": "esp32-demo",
            "temperature_c": 28.4,
            "humidity_pct": 61,
            "light_lux": 742,
            "voltage_v": 4.91,
        },
    )
    assert response.status_code == 201
    assert response.json()["accepted"] is True
    assert response.json()["device_id"] == "esp32-demo"
