# PulseLab architecture

```text
┌──────────────┐
│ ESP32 +      │
│ sensors      │
└──────┬───────┘
       │ telemetry
       ▼
┌──────────────┐
│ MQTT broker  │
└──────┬───────┘
       │
       ▼
┌──────────────┐       ┌──────────────┐
│ FastAPI      │──────▶│ PostgreSQL   │
│ ingestion    │       │ telemetry    │
└──────┬───────┘       └──────────────┘
       │ WebSocket
       ▼
┌──────────────┐
│ React        │
│ dashboard    │
└──────────────┘
```

## Current milestone

The repository currently has a working API contract for telemetry ingestion and a dashboard shell. Persistence, MQTT, WebSockets, and hardware integration are deliberately separated into later milestones.
