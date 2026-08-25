# PulseLab

Real-time IoT monitoring platform built around ESP32 sensor telemetry.

## Vision

PulseLab connects embedded hardware to a modern software dashboard so sensor data can be observed, stored, and analyzed in real time.

## Planned stack

- **Hardware:** ESP32 + environmental/motion sensors
- **Backend:** Python + FastAPI
- **Transport:** MQTT / WebSockets
- **Database:** SQLite → PostgreSQL
- **Frontend:** React + TypeScript
- **Charts:** Recharts

## Project status

🚧 Early development — foundation and architecture are being built.

## Roadmap

- [ ] FastAPI backend
- [ ] Sensor telemetry API
- [ ] Persistent data storage
- [ ] React dashboard
- [ ] Real-time WebSocket updates
- [ ] ESP32 firmware
- [ ] Alerts and anomaly detection
- [ ] Deployment

## Architecture

```text
ESP32 sensors → MQTT → FastAPI → Database
                              ↓
                         WebSocket
                              ↓
                       React Dashboard
```

## License

MIT
