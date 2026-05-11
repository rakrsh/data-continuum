# Run Data-Continuum ML Service locally as a process
$env:MLFLOW_TRACKING_URI = "http://localhost:5000"

Write-Host "Starting ML Service on http://localhost:8001..." -ForegroundColor Magenta
cd ml
uvicorn main:app --reload --port 8001
