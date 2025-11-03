from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, events, sessions, admin
from .db import Base, engine

# ensure DB schema created on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TESS Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth")
app.include_router(events.router, prefix="/api/events")
app.include_router(sessions.router, prefix="/api/sessions")
app.include_router(admin.router, prefix="/api/admin")

@app.get("/health")
def health():
    return {"status": "ok"}
