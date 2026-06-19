from sqlmodel import SQLModel, Field
from typing import Optional

class SessionExercise(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    session_id: int = Field(foreign_key="session.id")
    exercise_order: int
    exercise_def_id: int = Field(foreign_key="exercisedefinition.id")
    planned_sets: int
    planned_reps: int