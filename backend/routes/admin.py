from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
import os
from ..db import SessionLocal
from ..models import Event, Question, User
from typing import Optional
import json

router = APIRouter()
DATA_DIR = os.path.join(os.getcwd(), 'backend', 'data', 'events')

# simple helper to create admin user (for demo). In production you'd protect this more.
@router.post('/create-admin')
def create_admin(username: str, email: str, password: str):
    db = SessionLocal()
    try:
        u = db.query(User).filter((User.email==email) | (User.username==username)).first()
        if u:
            raise HTTPException(400, "User exists")
        from ..auth import hash_pw
        new = User(username=username, email=email, password_hash=hash_pw(password), is_active=True, is_admin=True)
        db.add(new); db.commit()
        return {'status':'created','id': new.id}
    finally:
        db.close()

@router.post('/{event_id}/upload-json')
def upload_event_json(event_id: str, file: UploadFile = File(...)):
    # Accept JSON file (diagnostic1.json etc)
    if not file.filename.lower().endswith('.json'):
        raise HTTPException(400, "Only JSON allowed")
    p = os.path.join(DATA_DIR, event_id)
    os.makedirs(p, exist_ok=True)
    dest = os.path.join(p, file.filename)
    with open(dest, 'wb') as f:
        f.write(file.file.read())
    # optional: validate basic JSON structure
    try:
        arr = json.load(open(dest))
        if not isinstance(arr, list):
            raise Exception("must be list")
    except Exception as e:
        os.remove(dest)
        raise HTTPException(400, f"Invalid JSON: {e}")
    return {'status':'ok','path': dest, 'count': len(arr)}


