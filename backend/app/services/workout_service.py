from sqlmodel import Session, select
from app.models.workout import Workout
from app.models.program import Program
from app.models.workout_exercise import WorkoutExercise
from app.models.exercise_definition import ExerciseDefinition
from app.schemas.workout import WorkoutDetailResponse, WorkoutExerciseInfo

def get_workout_details(workout_id: int, session: Session) -> WorkoutDetailResponse:
    workout = session.get(Workout, workout_id)

    if not workout:
        raise ValueError(f"Workout with id {workout_id} not found")
    
    program = session.get(Program, workout.program_id)
    workout_exercises = session.exec(select(WorkoutExercise).where(WorkoutExercise.workout_id == workout_id).order_by(WorkoutExercise.exercise_order)).all()

    exercise_list = []
    for workout_exercise in workout_exercises:
        exercise_definition = session.get(ExerciseDefinition, workout_exercise.exercise_def_id)
        exercise_list.append(WorkoutExerciseInfo(
            name=exercise_definition.name,
            planned_sets=workout_exercise.planned_sets,
            planned_reps=workout_exercise.planned_reps
        ))

    return WorkoutDetailResponse(
        program_name=program.name,
        program_day=workout.program_day,
        comments=workout.comments,
        exercises=exercise_list
    )

