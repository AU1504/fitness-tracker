from app.schemas.set import SetCreate, SetResponse
from app.services.set_service import log_set
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database.session import get_session

router = APIRouter()

@router.post("/sessions/{session_id}/sets", status_code=201, response_model=SetResponse)
def post_set(session_id: int, set_data: SetCreate, session: Session = Depends(get_session)):
    try:
        return log_set(session_id, set_data, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))