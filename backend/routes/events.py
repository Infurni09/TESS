from fastapi import APIRouter, HTTPException, UploadFile, File
import os, json

router = APIRouter()
DATA_DIR = os.path.join(os.getcwd(), 'backend', 'data', 'events')

@router.get('/list')
def list_events():
    if not os.path.exists(DATA_DIR):
        return {'events': []}
    events = [d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))]
    return {'events': events}

@router.get('/{event_id}/load_summary')
def load_summary(event_id: str):
    p = os.path.join(DATA_DIR, event_id)
    if not os.path.exists(p):
        raise HTTPException(404, 'event missing')
    summary = {}
    for fname in ['diagnostic1.json','diagnostic2.json','diagnostic3.json','practice_bank.json']:
        fp = os.path.join(p, fname)
        if os.path.exists(fp):
            try:
                arr = json.load(open(fp))
                summary[fname] = len(arr)
            except:
                summary[fname] = 'invalid'
        else:
            summary[fname] = 0
    return summary
