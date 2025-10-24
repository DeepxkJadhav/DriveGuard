import React, { useEffect, useState } from "react";
import MapView from "./components/MapView";
import AlertList from "./components/AlertList";

function App() {
  const [alerts, setAlerts] = useState([]);

  const fetchAlerts = async () => {
    try {
      const res = await fetch("http://localhost:8000/alerts");
      const data = await res.json();
      setAlerts(data);
    } catch (err) {
      console.error("Failed to fetch alerts:", err);
    }
  };

  useEffect(() => {
    fetchAlerts();
    const interval = setInterval(fetchAlerts, 5000); // refresh every 5s
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app-container">
      <h1>DriveGuard Dashboard</h1>
      <div className="dashboard">
        <MapView alerts={alerts} />
        <AlertList alerts={alerts} />
      </div>
    </div>
  );
}

export default App;
