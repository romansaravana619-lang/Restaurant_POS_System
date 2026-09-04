$ErrorActionPreference = "Stop"
Set-Location "$PSScriptRoot\05_Backend"

if (-not (Test-Path ".\venv\Scripts\python.exe")) {
    python -m venv venv
}

& ".\venv\Scripts\python.exe" -m pip install -r requirements.txt

if (-not $env:SARU_POS_JWT_SECRET) {
    $env:SARU_POS_JWT_SECRET = & ".\venv\Scripts\python.exe" -c "import secrets; print(secrets.token_urlsafe(32))"
}

& ".\venv\Scripts\python.exe" app.py
