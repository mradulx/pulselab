import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

const metrics = [
  ["Temperature", "28.4", "°C"],
  ["Humidity", "61", "%"],
  ["Light", "742", "lux"],
  ["Voltage", "4.91", "V"],
];

function App() {
  return (
    <main className="shell">
      <header>
        <div>
          <p className="eyebrow">PULSELAb / DEVICE MONITOR</p>
          <h1>Live telemetry</h1>
        </div>
        <span className="status"><i /> ESP32-DEMO ONLINE</span>
      </header>

      <section className="grid">
        {metrics.map(([label, value, unit]) => (
          <article className="card" key={label}>
            <span>{label}</span>
            <strong>{value}<small>{unit}</small></strong>
          </article>
        ))}
      </section>

      <section className="panel">
        <div className="panel-head">
          <div>
            <span>TELEMETRY</span>
            <h2>Waiting for live stream</h2>
          </div>
          <span className="muted">Last update: demo</span>
        </div>
        <div className="chart-placeholder">Connect an ESP32 to populate this chart.</div>
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(
  <StrictMode><App /></StrictMode>,
);
