# Observability

The Data-Continuum observability stack provides deep insights into the health, performance, and stability of the microservices.

## Components

### Prometheus
Prometheus is configured to scrape metrics from:
- **FastAPI Unified Extraction API** (`api:8000/metrics`)
- **FastAPI ML Service** (`ml:8001/metrics`)

### Grafana
Grafana connects directly to Prometheus to visualize system health, request latency, and HTTP response codes across the services.

### Accessing the UIs
- **Prometheus**: `http://localhost:9090`
- **Grafana**: `http://localhost:3000` (Default credentials: admin/admin)
