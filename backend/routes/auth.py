from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from ..db import SessionLocal, Base, engine
from ..models import User
from ..auth import hash_pw, verify_pw, create_access_token

# ensure tables created (safe idempotent)
Base.metadata.create_all(bind=engine)

router = APIRouter()

class RegisterIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_admin: bool = False

class LoginIn(BaseModel):
    identifier: str  # username OR email
    password: str

@router.post('/register')
def register(payload: RegisterIn):
    db = SessionLocal()
    try:
        if db.query(User).filter((User.email == payload.email) | (User.username == payload.username)).first():
            raise HTTPException(400, "User exists")
        u = User(
            username=payload.username,
            email=payload.email,
            password_hash=hash_pw(payload.password),
            is_active=True,
            is_admin=payload.is_admin
        )
        db.add(u); db.commit(); db.refresh(u)
        return {'id': u.id, 'email': u.email}
    finally:
        db.close()

@router.post('/login')
def login(payload: LoginIn):
    db = SessionLocal()
    try:
        # identifier can be email or username
        u = db.query(User).filter((User.email == payload.identifier) | (User.username == payload.identifier)).first()
        if not u or not verify_pw(payload.password, u.password_hash):
            raise HTTPException(401, "Invalid credentials")
        token = create_access_token({'sub': u.id, 'email': u.email, 'is_admin': bool(u.is_admin)})
        return {'access_token': token, 'token_type': 'bearer', 'is_admin': bool(u.is_admin)}
    finally:
        db.close()
