# Run Data-Continuum API locally as a process
$env:POSTGRES_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/continuum"
$env:MONGO_URL = "mongodb://admin:admin@localhost:27017/"

Write-Host "Starting API on http://localhost:8000..." -ForegroundColor Cyan
cd api
uvicorn main:app --reload --port 8000
