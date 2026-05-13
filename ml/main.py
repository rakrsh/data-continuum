import os
from fastapi import FastAPI, BackgroundTasks
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
import numpy as np
from prometheus_fastapi_instrumentator import Instrumentator

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize MLflow
    mlflow_uri = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
    mlflow.set_tracking_uri(mlflow_uri)
    try:
        mlflow.set_experiment("predictive_eta")
        print(f"MLflow initialized with URI: {mlflow_uri}")
    except Exception as e:
        print(f"Warning: Failed to connect to MLflow at {mlflow_uri}: {e}")
    yield


app = FastAPI(title="Data-Continuum ML Service", lifespan=lifespan)

Instrumentator().instrument(app).expose(app)


def train_model():
    print("Starting ML training job...")
    with mlflow.start_run():
        # Dummy data for demonstration
        X = np.random.rand(100, 2) * 100  # Features: distance, traffic_score
        y = X[:, 0] * 0.5 + X[:, 1] * 0.2 + np.random.rand(100) * 10  # ETA

        model = LinearRegression()
        model.fit(X, y)

        score = model.score(X, y)
        mlflow.log_metric("r2_score", score)
        mlflow.sklearn.log_model(model, "model")
        print(f"Training completed. R2 Score: {score}")


@app.post("/train")
async def trigger_training(background_tasks: BackgroundTasks):
    background_tasks.add_task(train_model)
    return {"message": "Training job triggered in background."}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
