# Architecture

The Data-Continuum architecture is built on a Polyglot Persistence pattern with an Event-Driven Orchestration layer. 

## System Components

### 1. Data Ingestion Layer (The Source)
* **Relational Storage (SQL):** PostgreSQL 15+ storing transactional shipment data (IDs, Customer info, Status, timestamps).
* **Non-Relational Storage (NoSQL):** MongoDB storing high-frequency vehicle telemetry (GPS coordinates, engine sensors, fuel levels).

### 2. Orchestration & Engineering Layer (The Brain)
* **Workflow Engine:** Apache Airflow.
* **Core Responsibilities:**
    * Monitor database health sensors.
    * Trigger periodic PySpark jobs for data cleaning.
    * Handle retry logic for failed extraction tasks.

### 3. Service & ML Layer (The Interface)
* **Unified Extraction API:** FastAPI service to retrieve "Unified Shipment State".
* **ML Training Service:** FastAPI endpoint to trigger training of a Predictive ETA model.
* **Experiment Tracking:** MLflow integration to log model versions and accuracy metrics.

### 4. Observability & UI Layer (The Monitor)
* **Metrics:** Prometheus scraping API and DB performance.
* **Visualization:** Grafana dashboards for system health.

## Infrastructure

The entire stack is containerized using Docker and Docker Compose, connected via an isolated internal bridge network for data services, with exposed gateways for the API/UI.
