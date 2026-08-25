# ESP32 firmware

This directory will contain the ESP32 firmware that publishes PulseLab telemetry.

Planned sensors:

- BME280/DHT22 — temperature + humidity
- LDR — light level
- INA219 or ADC — voltage/current
- Optional PIR — motion

The first firmware milestone is a stable heartbeat plus telemetry payload published to the backend transport.
