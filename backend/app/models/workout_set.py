from sqlmodel import SQLModel, Field
from typing import Optional

class WorkoutSet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_exercise_id: int = Field(foreign_key="sessionexercise.id")
    reps: int
    weight: float
    comments: Optional[str] = Field(default=None)