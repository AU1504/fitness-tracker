from datetime import datetime
from sqlmodel import SQLModel

class PRResponse(SQLModel):
    exercise_name: str
    pr_date: datetime
    pr_weight: float