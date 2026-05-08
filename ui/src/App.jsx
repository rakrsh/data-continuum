import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [shipmentId, setShipmentId] = useState('');
  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  const fetchShipment = async (e) => {
    e.preventDefault();
    try {
      setError('');
      const response = await axios.get(`http://localhost:8000/shipments/${shipmentId}/unified`);
      setData(response.data);
    } catch (err) {
      setError('Failed to fetch shipment. Ensure API is running and ID is valid.');
      setData(null);
    }
  };

  return (
    <div className="container">
      <header className="header">
        <h1>Data-Continuum Logistics</h1>
        <p>Premium Real-Time Shipment Tracking</p>
      </header>
      
      <main className="main-content">
        <form onSubmit={fetchShipment} className="search-form">
          <input
            type="number"
            placeholder="Enter Shipment ID"
            value={shipmentId}
            onChange={(e) => setShipmentId(e.target.value)}
            className="search-input"
          />
          <button type="submit" className="btn">Track</button>
        </form>

        {error && <div className="error">{error}</div>}

        {data && (
          <div className="card-grid">
            <div className="card glass-effect">
              <h2>Shipment Status</h2>
              <p className="status-badge">{data.status}</p>
              <p><strong>Customer:</strong> {data.customer_name}</p>
              <p><strong>ID:</strong> {data.shipment_id}</p>
            </div>
            
            <div className="card glass-effect">
              <h2>Real-Time Telemetry</h2>
              <div className="telemetry-grid">
                <div>
                  <span className="label">Location</span>
                  <span className="value">{data.latitude?.toFixed(4)}, {data.longitude?.toFixed(4)}</span>
                </div>
                <div>
                  <span className="label">Engine Temp</span>
                  <span className="value">{data.engine_temp?.toFixed(1)} °C</span>
                </div>
                <div>
                  <span className="label">Fuel Level</span>
                  <span className="value">{data.fuel_level?.toFixed(1)} %</span>
                </div>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
