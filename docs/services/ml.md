# ML Training Service

The ML Training Service is a **FastAPI** application dedicated to Machine Learning orchestration and model training.

## Endpoints

### `POST /train`
Triggers a background task to train a Predictive ETA model (using Scikit-Learn). It simulates feature extraction from the combined SQL/NoSQL stores.

## MLflow Integration
The service integrates natively with an MLflow tracking server to log experiment runs, model versions, and accuracy metrics (e.g., R2 Score). All metrics are stored and viewable in the MLflow UI (`http://localhost:5000`).

### Metrics
The service exposes standard Prometheus metrics out-of-the-box via `prometheus-fastapi-instrumentator`.
