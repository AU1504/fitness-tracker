from app.models.user import User
from app.models.user_program import UserProgram
from sqlmodel import Session, select
from app.models.workout import Workout
from app.models.session import Session as WorkoutSession
from app.models.program import Program
from app.models.workout_exercise import WorkoutExercise
from app.models.exercise_definition import ExerciseDefinition
from app.schemas.workout import NextWorkoutResponse, WorkoutDetailResponse, WorkoutExerciseInfo

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

def get_next_workout(session: Session) -> NextWorkoutResponse:
    find_user = session.exec(select(User)).first()
    user_program = session.exec(select(UserProgram).where(UserProgram.user_id == find_user.id)).first()

    if not user_program:
        raise ValueError(f"User program for user with id {find_user.id} not found")
    
    last_session = session.exec(select(WorkoutSession).order_by(WorkoutSession.date.desc())).first()

    if last_session is None:
        next_day = 1
    else:
        last_workout = session.get(Workout, last_session.workout_id)
        total_days = len(session.exec(select(Workout).where(Workout.program_id == user_program.program_id)).all())
        next_day = (last_workout.program_day % total_days) + 1
    
    next_workout = session.exec(select(Workout).where((Workout.program_id == user_program.program_id) & (Workout.program_day == next_day))).first()

    return NextWorkoutResponse(
        workout_id=next_workout.id,
        program_name=session.get(Program, next_workout.program_id).name,
        program_day=next_workout.program_day,
        comments=next_workout.comments
    )