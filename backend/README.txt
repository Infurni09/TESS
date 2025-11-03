TESS Backend (SQLite default) - Quickstart

1) Copy this backend/ folder into your repo root so path is TESS/backend/
2) Ensure your existing backend/data/events/ folder (your DECA question banks) remains in the repo and is NOT overwritten.
3) Create a virtualenv and install requirements:
   python -m venv venv
   # Windows PowerShell:
   .\venv\Scripts\Activate
   pip install --upgrade pip
   pip install -r requirements.txt
4) Run the backend:
   uvicorn app.main:app --reload --port 8000
5) API quick endpoints:
   GET /health
   POST /api/auth/register  {username,email,password}
   POST /api/auth/login     {email,password}
   GET  /api/events/list
   POST /api/events/{event_id}/load_summary
   POST /api/sessions/start/{user_id}/{event_id}?mode=diagnostic&which=1
   POST /api/sessions/submit/{session_id}?user_id=1&event_id=Sample_Arithmetic&question_id=1&selected=12
