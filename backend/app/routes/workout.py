from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database.session import get_session
from app.services.workout_service import get_workout_details
from app.schemas.workout import WorkoutDetailResponse

router = APIRouter()

@router.get("/workouts/{workout_id}", response_model=WorkoutDetailResponse)
def read_workout(workout_id: int, session: Session = Depends(get_session)):
    try:
       return get_workout_details(workout_id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))