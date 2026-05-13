import os
from fastapi.testclient import TestClient
from ml.main import app

# Use a local file-based tracking URI for tests to avoid connection errors
os.environ["MLFLOW_TRACKING_URI"] = "file:./mlruns"


client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_trigger_training():
    response = client.post("/train")
    assert response.status_code == 200
    assert "Training job triggered" in response.json().get("message", "")
