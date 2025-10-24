import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";

// Fix default marker icon for React-Leaflet
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png",
  iconUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png",
  shadowUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png"
});

function MapView({ alerts }) {
  const defaultPosition = [37.7749, -122.4194]; // SF

  return (
    <MapContainer center={defaultPosition} zoom={14} style={{ height: "500px", width: "100%" }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {alerts.map(alert => (
        <Marker key={alert.id} position={[alert.latitude, alert.longitude]}>
          <Popup>
            <strong>Timestamp:</strong> {new Date(alert.timestamp * 1000).toLocaleString()}<br/>
            <strong>Hazards:</strong> {alert.hazards.map(h => h.type).join(", ")}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}

export default MapView;
