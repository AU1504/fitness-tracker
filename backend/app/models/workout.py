from sqlmodel import SQLModel, Field
from typing import Optional

class Workout(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    program_id: int = Field(foreign_key="program.id")
    program_day: int
    comments: Optional[str] = None