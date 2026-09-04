# SaruPOS Final Fix Notes — 2026-09-04

## Fixes included
- API tests now use unique customer phone numbers so SQLite UNIQUE constraints do not make unrelated tests fail.
- Customer IDs remain server-generated (`CUSTxxxxxx`); tests no longer send client-generated customer IDs.
- Checkout service test adds `05_Backend` to `sys.path` before importing `connection`.
- Checkout test schema uses `email TEXT UNIQUE` for employees.
- Existing backend checkout flow and frontend checkout integration are preserved.

## Local verification
1. Open this project root in VS Code.
2. In `05_Backend`, create/activate `venv` and install `requirements.txt`.
3. Set `SARU_POS_JWT_SECRET`.
4. Start `python app.py`.
5. From the project root, activate the same venv and run:
   `pytest -q tests`
6. Then start the frontend with `npm install` and `npm run dev`.
