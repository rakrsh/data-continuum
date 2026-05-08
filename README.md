# Data-Continuum

Data-Continuum is a production-grade data pipeline sandbox designed to simulate a high-velocity Smart Logistics environment. It demonstrates the seamless flow of data from diverse sources (SQL and NoSQL) through an orchestration layer into a unified API and Machine Learning service.

## Architecture

* **Databases:** PostgreSQL (Relational) and MongoDB (NoSQL)
* **Orchestration:** Apache Airflow
* **Microservices:** FastAPI for API and ML services
* **Observability:** Prometheus, Grafana, MLflow

## Getting Started

### Prerequisites

* Docker & Docker Compose
* Python 3.10+ (optional, for local development)
* `uv` for fast package management

### Running the Environment

You can spin up the entire Data-Continuum ecosystem using Docker Compose:

```bash
docker-compose up --build -d
```

### Accessing Services

* **Airflow UI:** `http://localhost:8080` (admin/admin)
* **Unified API (Swagger):** `http://localhost:8000/docs`
* **MLflow Tracking Server:** `http://localhost:5000`
* **Prometheus:** `http://localhost:9090`
* **Grafana:** `http://localhost:3000` (admin/admin)

## Documentation

Full documentation is available via MkDocs. To view it locally:

```bash
uv pip install -e .[docs]
mkdocs serve
```

## Development

For local development and testing, install the development dependencies:

```bash
uv pip install -e .[dev]
pre-commit install
```
