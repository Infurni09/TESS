# 📚 TESS — Test Evaluation Support System
TESS is an ML-driven diagnostic testing platform designed to identify topic weaknesses, generate targeted practice, track mastery growth, and transition users into holistic testing once mastery is achieved.

This README explains how to run TESS locally on **Windows**, **Mac**, or **Linux**.

---

## ✅ Features
- Multi-event support (e.g., DECA clusters)
- 3-Phase Learning Model:
  ✅ Diagnostic → Targeted Practice → Holistic Testing
- Machine Learning:
  ✅ Bayesian Knowledge Tracing (BKT)
  ✅ Mastery threshold default = 0.95
- Local authentication + role support:
  ✅ Student / Admin
- Admin upload interface ready (API done, UI coming)
- Mastery dashboard with charts
- SQLite persistent learning database

---

## 🧱 Project Structure






**IMPORTANT**  
✅ Do **not** delete or overwrite:  
`backend/data/events` → contains your event question JSON files

---

# 🚀 How to Run Locally

You will use **two terminals**:

✅ One for backend  
✅ One for frontend

---

## 🖥 Windows Instructions

### 🔹 Backend (Terminal #1)
```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000


##### Frontend (Terminal 2)
cd frontend
npm install
npm run dev



Mac/Linux Instructions

Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000



Frontend
cd frontend
npm install
npm run dev
