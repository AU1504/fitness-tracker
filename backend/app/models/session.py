from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone

class Session(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    workout_id: int = Field(foreign_key="workout.id")
    comments: Optional[str] = Field(default=None)
    completed: bool = Field(default=False)
    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))