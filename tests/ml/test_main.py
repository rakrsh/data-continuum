from fastapi.testclient import TestClient
from ml.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_trigger_training():
    response = client.post("/train")
    assert response.status_code == 200
    assert "Training job triggered" in response.json().get("message", "")
