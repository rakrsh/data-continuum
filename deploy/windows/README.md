# Windows Native Deployment

This guide explains how to deploy Data-Continuum services as native Windows background processes (Services) without using containers.

## Prerequisites
- **Python 3.12+** installed and added to PATH.
- **Node.js** installed for the UI.
- **NSSM (Non-Sucking Service Manager)**: Download from [nssm.cc](https://nssm.cc/download) and add it to your PATH.
- **PostgreSQL** and **MongoDB** installed and running on Windows.

## 1. Environment Setup
Create a virtual environment and install dependencies:

```powershell
uv venv
.\.venv\Scripts\activate
uv pip install -r api/requirements.txt
uv pip install -r ml/requirements.txt
```

## 2. Local Execution (Process-based)
For development or manual execution, use the provided scripts in the `scripts/` directory:

```powershell
# Start all services in separate terminal windows
.\scripts\start_all.ps1
```

## 3. Registering as Windows Services
You can use `nssm` to register the API and ML services to start automatically with Windows.

### API Service
```powershell
nssm install DC_API "C:\Path\To\Project\.venv\Scripts\python.exe"
nssm set DC_API AppDirectory "C:\Path\To\Project\api"
nssm set DC_API AppParameters "-m uvicorn main:app --port 8000"
nssm set DC_API AppStdout "C:\Path\To\Project\logs\api.log"
nssm set DC_API AppStderr "C:\Path\To\Project\logs\api_error.log"
nssm start DC_API
```

### ML Service
```powershell
nssm install DC_ML "C:\Path\To\Project\.venv\Scripts\python.exe"
nssm set DC_ML AppDirectory "C:\Path\To\Project\ml"
nssm set DC_ML AppParameters "-m uvicorn main:app --port 8001"
nssm set DC_ML AppStdout "C:\Path\To\Project\logs\ml.log"
nssm set DC_ML AppStderr "C:\Path\To\Project\logs\ml_error.log"
nssm start DC_ML
```

## 4. Serving the UI
For a production-like Windows deployment, build the UI and serve it using a web server like IIS, Caddy, or Nginx for Windows.

```powershell
cd ui
npm install
npm run build
```
Copy the contents of `ui/dist` to your web server's root.
