from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database.session import get_session
from app.services.session_service import start_session
from app.schemas.session import SessionStartResponse

router = APIRouter()

@router.post("/workouts/{workout_id}/start", status_code=201, response_model=SessionStartResponse)
def post_workout_session(workout_id: int, session: Session = Depends(get_session)):
    try:
        return start_session(workout_id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
