import React from "react";

function AlertList({ alerts }) {
  return (
    <div className="alert-list">
      <h2>Recent Alerts</h2>
      {alerts.length === 0 && <p>No alerts yet.</p>}
      <ul>
        {alerts.map(alert => (
          <li key={alert.id}>
            <strong>Time:</strong> {new Date(alert.timestamp * 1000).toLocaleString()}<br/>
            <strong>Location:</strong> {alert.latitude.toFixed(5)}, {alert.longitude.toFixed(5)}<br/>
            <strong>Hazards:</strong> {alert.hazards.map(h => `${h.type} (${h.confidence.toFixed(2)})`).join(", ")}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AlertList;
