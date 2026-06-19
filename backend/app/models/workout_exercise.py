from sqlmodel import SQLModel, Field
from typing import Optional

class WorkoutExercise(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    workout_id: int = Field(foreign_key="workout.id")
    exercise_def_id: int = Field(foreign_key="exercisedefinition.id")
    exercise_order: int
    planned_sets: int
    planned_reps: int