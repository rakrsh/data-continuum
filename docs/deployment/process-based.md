# Process-based Deployment

This guide explains how to run Data-Continuum services as standalone OS processes. This is the simplest way to run the project without Docker or Kubernetes.

## Prerequisites
- **Python 3.12+**
- **Node.js**
- Local instances of **PostgreSQL**, **MongoDB**, and **Redis**.

## Setup

1. **Install Python Dependencies**:
   ```bash
   uv venv
   source .venv/bin/activate  # Or .\.venv\Scripts\activate on Windows
   uv pip install -r api/requirements.txt
   uv pip install -r ml/requirements.txt
   ```

2. **Install UI Dependencies**:
   ```bash
   cd ui
   npm install
   cd ..
   ```

## Running Services

### Using Helper Scripts (Windows)
If you are on Windows, you can use the PowerShell scripts in the `scripts/` directory:

```powershell
.\scripts\start_all.ps1
```

### Manual Execution

#### 1. Start the API
```bash
export POSTGRES_URL="postgresql+asyncpg://postgres:postgres@localhost:5432/continuum"
export MONGO_URL="mongodb://admin:admin@localhost:27017/"
cd api
uvicorn main:app --reload --port 8000
```

#### 2. Start the ML Service
```bash
export MLFLOW_TRACKING_URI="http://localhost:5000"
cd ml
uvicorn main:app --reload --port 8001
```

#### 3. Start the UI
```bash
cd ui
npm run dev
```

## Configuration
Services use environment variables for configuration. You can also create a `.env` file in the root directory, though the current implementation primarily relies on direct environment variables or defaults in the code.
