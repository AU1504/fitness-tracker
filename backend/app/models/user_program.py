from sqlmodel import SQLModel, Field
from typing import Optional

class UserProgram(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    program_id: int = Field(foreign_key="program.id", primary_key=True)
    week: Optional[int] = Field(default=None)
    progression: Optional[int] = Field(default=None)