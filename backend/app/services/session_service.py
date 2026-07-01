from sqlmodel import Session, select
from app.models.workout import Workout
from app.models.program import Program
from app.models.workout_exercise import WorkoutExercise
from app.models.session import Session as WorkoutSession
from app.models.session_exercise import SessionExercise
from app.models.exercise_definition import ExerciseDefinition
from app.schemas.session import SessionStartResponse
from app.schemas.session import SessionExerciseInfo

def start_session(workout_id: int, session: Session) -> SessionStartResponse:
    workout = session.get(Workout, workout_id)

    if not workout:
        raise ValueError(f"Workout with id {workout_id} not found")
    
    program = session.get(Program, workout.program_id)
    workout_exercises = session.exec(select(WorkoutExercise).where(WorkoutExercise.workout_id == workout_id).order_by(WorkoutExercise.exercise_order)).all()

    # Create a new session
    new_session = WorkoutSession(workout_id=workout_id)
    session.add(new_session)
    session.commit()
    session.refresh(new_session)

    exercise_list = []
    for workout_exercise in workout_exercises:
        exercise_definition = session.get(ExerciseDefinition, workout_exercise.exercise_def_id)

        # Create a new session exercise entry
        new_session_exercise = SessionExercise(
            session_id=new_session.id,
            exercise_order=workout_exercise.exercise_order,
            exercise_def_id=workout_exercise.exercise_def_id,
            planned_sets=workout_exercise.planned_sets,
            planned_reps=workout_exercise.planned_reps
        )

        session.add(new_session_exercise)
        session.flush()  # Flush to get the ID of the new session exercise
        session.refresh(new_session_exercise)

        exercise_list.append(SessionExerciseInfo(
            session_exercise_id=new_session_exercise.id,
            name=exercise_definition.name,
            planned_sets=workout_exercise.planned_sets,
            planned_reps=workout_exercise.planned_reps
        ))

    session.commit()

    return SessionStartResponse(
        session_id=new_session.id,
        date=new_session.date,
        program_name=program.name,
        program_day=workout.program_day,
        comments=workout.comments,
        exercises=exercise_list
    )