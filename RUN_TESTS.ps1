$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path ".\05_Backend\venv\Scripts\python.exe")) {
    Write-Host "Backend venv not found. Run START_BACKEND.ps1 once first."
    exit 1
}

& ".\05_Backend\venv\Scripts\python.exe" -m pytest -q tests
