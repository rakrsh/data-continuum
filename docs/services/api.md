# Unified Extraction API

The Unified Extraction API is built using **FastAPI** and serves as the single point of truth to retrieve the "Unified Shipment State".

## Endpoints

### `GET /shipments/{shipment_id}/unified`
This endpoint queries both the relational PostgreSQL database for shipment metadata and the NoSQL MongoDB database for the latest telemetry payload. It combines them into a single `UnifiedState` Pydantic model response.

### `GET /health`
Standard health check endpoint to ensure the service is running.

### Metrics
The API exposes standard Prometheus metrics out-of-the-box via `prometheus-fastapi-instrumentator`.
