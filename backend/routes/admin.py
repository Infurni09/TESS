from fastapi import APIRouter

router = APIRouter()

@router.post('/retrain')
def retrain():
    # placeholder - in production would enqueue trainer job
    return {'status': 'queued'}
