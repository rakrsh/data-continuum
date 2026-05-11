# Helper script to register Data-Continuum services using NSSM
# Run this script as Administrator

$ProjectRoot = Get-Location
$VenvPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $VenvPython)) {
    Write-Error "Virtual environment not found at $VenvPython. Please create it first."
    exit 1
}

function Install-DCService($Name, $Dir, $Params) {
    Write-Host "Installing $Name..." -ForegroundColor Cyan
    nssm install $Name $VenvPython
    nssm set $Name AppDirectory (Join-Path $ProjectRoot $Dir)
    nssm set $Name AppParameters "-m uvicorn main:app $Params"
    nssm set $Name AppStdout (Join-Path $ProjectRoot "logs\$Name.log")
    nssm set $Name AppStderr (Join-Path $ProjectRoot "logs\$Name`_error.log")
    Write-Host "$Name installed successfully." -ForegroundColor Green
}

# Ensure logs directory exists
if (-not (Test-Path "logs")) { New-Item -ItemType Directory "logs" }

# Install Services
Install-DCService "DC_API" "api" "--port 8000"
Install-DCService "DC_ML" "ml" "--port 8001"

Write-Host "Services installed. Use 'nssm start <service_name>' to start them." -ForegroundColor Yellow
