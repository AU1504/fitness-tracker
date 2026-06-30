from datetime import datetime
from app.schemas.workout import WorkoutExerciseInfo
from sqlmodel import SQLModel
from typing import List, Optional

class SessionStartResponse(SQLModel):
    session_id: int
    date: datetime
    program_name: str
    program_day: int
    comments: Optional[str]
    exercises: List[WorkoutExerciseInfo]