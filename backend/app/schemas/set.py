from sqlmodel import SQLModel
from typing import Optional

class SetCreate(SQLModel):
    session_exercise_id: int
    weight: float
    reps: int
    comments: Optional[str] = None

class SetResponse(SQLModel):
    set_id: int
    reps: int
    weight: float
    comments: Optional[str] = None
    is_pr: bool