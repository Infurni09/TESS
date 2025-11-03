from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from ..db import SessionLocal, Base, engine
from ..models import User
from ..auth import hash_pw, verify_pw, create_access_token

Base.metadata.create_all(bind=engine)

router = APIRouter()

class RegisterIn(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginIn(BaseModel):
    email: EmailStr
    password: str

@router.post('/register')
def register(payload: RegisterIn):
    db = SessionLocal()
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(400, 'Email exists')
    u = User(username=payload.username, email=payload.email, password_hash=hash_pw(payload.password), is_active=True)
    db.add(u); db.commit(); db.refresh(u)
    return {'id': u.id, 'email': u.email}

@router.post('/login')
def login(payload: LoginIn):
    db = SessionLocal()
    u = db.query(User).filter(User.email == payload.email).first()
    if not u or not verify_pw(payload.password, u.password_hash):
        raise HTTPException(401, 'Invalid credentials')
    token = create_access_token({'sub': u.id, 'email': u.email})
    return {'access_token': token, 'token_type': 'bearer'}
