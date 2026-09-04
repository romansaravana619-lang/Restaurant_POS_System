# Saru POS — Local Run

## Backend

```powershell
cd 05_Backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:SARU_POS_JWT_SECRET = "replace-with-a-random-secret-at-least-32-characters"
python create_tables.py
python seed_data.py
python app.py
```

Backend: `http://127.0.0.1:5000`

## Frontend

Open a second terminal:

```powershell
cd 06_Frontend
npm install
npm run dev
```

Frontend: `http://127.0.0.1:5173`

Default seeded login: `admin` / `admin123`. Change it after first login in a production deployment.

## Validation

- Backend source compilation: `python -m compileall 05_Backend`
- Backend API suite: start the backend, then `pytest -q tests`
- Frontend: `npm run lint` and `npm run build`
