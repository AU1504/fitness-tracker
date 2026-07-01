from datetime import datetime
from sqlmodel import SQLModel
from typing import List, Optional

class SessionExerciseInfo(SQLModel):
    session_exercise_id: int
    name: str
    planned_sets: int
    planned_reps: int
    
class SessionStartResponse(SQLModel):
    session_id: int
    date: datetime
    program_name: str
    program_day: int
    comments: Optional[str]
    exercises: List[SessionExerciseInfo]