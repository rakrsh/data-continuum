# Data-Continuum

Welcome to the **Data-Continuum** documentation.

Data-Continuum is a production-grade data pipeline sandbox designed to simulate a high-velocity Smart Logistics environment. It demonstrates the seamless flow of data from diverse sources (SQL and NoSQL) through an orchestration layer into a unified API and Machine Learning service, all while maintained under a rigorous observability stack.

## Key Features

- **Polyglot Persistence**: Combines relational metadata (PostgreSQL) with high-frequency telemetry (MongoDB).
- **Event-Driven Orchestration**: Powered by Apache Airflow.
- **Unified Extraction**: A FastAPI layer to combine SQL and NoSQL data into a single unified state.
- **ML Integration**: Integrated MLflow tracking with background training capabilities.
- **Observability**: Prometheus metrics and Grafana dashboards out-of-the-box.

Get started by exploring the [Architecture](architecture.md).
