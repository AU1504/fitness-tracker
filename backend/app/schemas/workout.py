from sqlmodel import SQLModel
from typing import List, Optional

class WorkoutExerciseInfo(SQLModel):
    name: str
    planned_sets: int
    planned_reps: int

class WorkoutDetailResponse(SQLModel):
    program_name: str
    program_day: int
    comments: Optional[str]
    exercises: List[WorkoutExerciseInfo]