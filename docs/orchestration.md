# Orchestration

Data-Continuum uses **Apache Airflow** as its central orchestration engine.

Airflow is responsible for scheduling, monitoring, and triggering the various data pipelines and training services within the ecosystem.

## DAGs

### `data_continuum_pipeline`
A daily scheduled pipeline that performs the following tasks:
1. **Verify Connections**: Ensures PostgreSQL and MongoDB are accessible.
2. **Run PySpark Cleaning**: Simulates a spark-submit job to clean and join data across the polyglot databases.
3. **Trigger ML Training**: Sends an HTTP request to the ML Service (`http://api:8001/train`) to automatically start a new round of predictive ETA training.
