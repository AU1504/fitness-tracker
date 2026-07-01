from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone

class Pr(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    set_id: int = Field(foreign_key="workoutset.id")
    user_id: int = Field(foreign_key="user.id")
    exercise_def_id: int = Field(foreign_key="exercisedefinition.id")
    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))