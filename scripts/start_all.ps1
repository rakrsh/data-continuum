# Start all Data-Continuum services in separate windows
Write-Host "Launching Data-Continuum Services..." -ForegroundColor Yellow

# Start API
Start-Process powershell -ArgumentList "-NoExit", "-Command", "powershell .\scripts\run_api.ps1" -WindowStyle Normal

# Start ML
Start-Process powershell -ArgumentList "-NoExit", "-Command", "powershell .\scripts\run_ml.ps1" -WindowStyle Normal

# Start UI
Start-Process powershell -ArgumentList "-NoExit", "-Command", "powershell .\scripts\run_ui.ps1" -WindowStyle Normal

Write-Host "Services are launching. Check separate terminal windows." -ForegroundColor Green
