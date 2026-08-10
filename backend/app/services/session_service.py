from app.models.pr import Pr
from app.models.workout_set import WorkoutSet
from sqlmodel import Session, select
from app.models.workout import Workout
from app.models.program import Program
from app.models.workout_exercise import WorkoutExercise
from app.models.session import Session as WorkoutSession
from app.models.session_exercise import SessionExercise
from app.models.exercise_definition import ExerciseDefinition
from app.schemas.session import PreviousExerciseInfo, PreviousSessionResponse, PreviousSetInfo, SessionStartResponse
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

def get_previous_session(session_id: int, session: Session) -> PreviousSessionResponse:
    workout_session = session.get(WorkoutSession, session_id)

    if not workout_session:
        raise ValueError(f"Session with id {session_id} not found")
    
    workout = session.get(Workout, workout_session.workout_id)

    previous_session = session.exec(select(WorkoutSession).where(
        (WorkoutSession.workout_id == workout.id) & 
        (WorkoutSession.id != workout_session.id)
    ).order_by(WorkoutSession.date.desc())).first()

    if not previous_session:
        raise ValueError(f"No previous session found for workout with id {workout.id}")
    
    program = session.get(Program, workout.program_id)
    previous_session_exercises = session.exec(select(SessionExercise).where(SessionExercise.session_id == previous_session.id).order_by(SessionExercise.exercise_order)).all()

    previous_exercises = []
  
    for exercise in previous_session_exercises:
        set_list = []
        exercise_definition = session.get(ExerciseDefinition, exercise.exercise_def_id)
        workout_sets = session.exec(select(WorkoutSet).where(WorkoutSet.session_exercise_id == exercise.id)).all()

        for set_number, workout_set in enumerate(workout_sets, start=1):
            pr_record = session.exec(select(Pr).where(Pr.set_id == workout_set.id)).first()
            is_pr = pr_record is not None

            previous_set_info = PreviousSetInfo(
                set_number=set_number,
                reps=workout_set.reps,
                weight=workout_set.weight,
                is_pr=is_pr
            )
            set_list.append(previous_set_info)
        
        previous_exercise_info = PreviousExerciseInfo(
            name=exercise_definition.name,
            sets=set_list
        )

        previous_exercises.append(previous_exercise_info)

    return PreviousSessionResponse(
        session_date=previous_session.date,
        program_name=program.name,
        program_day=workout.program_day,
        comments=workout.comments,
        exercises=previous_exercises
    ) 

def get_session(session_id: int, session: Session) -> SessionStartResponse:
    workout_session = session.get(WorkoutSession, session_id)
    if not workout_session:
        raise ValueError(f"Session with id {session_id} not found")
    curr_workout = session.get(Workout, workout_session.workout_id)  # Ensure the workout is loaded
    curr_program = session.get(Program, curr_workout.program_id)  # Ensure the program is loaded

    session_exercises = session.exec(
    select(SessionExercise)
    .where(SessionExercise.session_id == session_id)
    .order_by(SessionExercise.exercise_order)
    ).all()

    exercise_list = []
    for se in session_exercises:
        exercise_def = session.get(ExerciseDefinition, se.exercise_def_id)
        exercise_list.append(SessionExerciseInfo(
            session_exercise_id=se.id,
            name=exercise_def.name,
            planned_sets=se.planned_sets,
            planned_reps=se.planned_reps
        ))

    return SessionStartResponse(
        session_id=workout_session.id,
        date=workout_session.date,
        program_name=curr_program.name,
        program_day=curr_workout.program_day,
        comments=curr_workout.comments,
        exercises=exercise_list
    )


