from fastapi import APIRouter, HTTPException
import os, json, random
from ..ml.bkt import BKT, MASTERY_THRESHOLD
from ..db import SessionLocal
from ..models import Mastery

router = APIRouter()
DATA_DIR = os.path.join(os.getcwd(), 'backend', 'data', 'events')
bkt_model = BKT()

@router.post('/start/{user_id}/{event_id}')
def start(user_id: int, event_id: str, mode: str = 'diagnostic', which: int = 1):
    pool = f'diagnostic{which}.json' if mode=='diagnostic' else 'practice_bank.json'
    fp = os.path.join(DATA_DIR, event_id, pool)
    if not os.path.exists(fp):
        raise HTTPException(404, 'pool missing')
    arr = json.load(open(fp))
    if not arr:
        raise HTTPException(404, 'empty pool')
    q = random.choice(arr)
    return {'session_id': 1, 'question': {'id': q.get('id',0), 'question': q.get('question'), 'choices': q.get('choices',[]), 'topic': q.get('topic','General'), 'subtopic': q.get('subtopic', q.get('topic','General'))}}

@router.post('/submit/{session_id}')
def submit(session_id: int, user_id: int, event_id: str, question_id: int, selected: str):
    p = os.path.join(DATA_DIR, event_id)
    found = None
    for fname in ['diagnostic1.json','diagnostic2.json','diagnostic3.json','practice_bank.json']:
        fp = os.path.join(p, fname)
        if os.path.exists(fp):
            try:
                arr = json.load(open(fp))
                for q in arr:
                    if q.get('id') == question_id:
                        found = q; break
            except: pass
        if found: break
    correct = False
    if found and str(found.get('answer')) == str(selected):
        correct = True
    # update mastery
    db = SessionLocal()
    try:
        topic = found.get('topic') if found else 'General'
        subtopic = found.get('subtopic') if found else topic
        m = db.query(Mastery).filter(Mastery.user_id==user_id, Mastery.event==event_id, Mastery.topic==topic, Mastery.subtopic==subtopic).first() if found else None
        prior = m.prob if (m and m.prob) else 0.2
        newp = bkt_model.update(prior, correct)
        if m:
            m.prob = newp; db.add(m)
        else:
            nm = Mastery(user_id=user_id, event=event_id, topic=topic, subtopic=subtopic, prob=newp)
            db.add(nm)
        db.commit()
    finally:
        db.close()
    ready_for_holistic = newp >= MASTERY_THRESHOLD
    return {'correct': correct, 'new_mastery': newp, 'ready_for_holistic': ready_for_holistic}
