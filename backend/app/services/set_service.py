from app.models.session_exercise import SessionExercise
from app.models.workout_set import WorkoutSet
from app.schemas.set import SetCreate, SetResponse
from app.services.pr_service import check_and_create_pr
from app.models.user import User
from sqlmodel import Session, select

def log_set(session_id: int, data: SetCreate, session: Session) -> SetResponse:

    find_user = session.exec(select(User)).first()
    if not find_user:
        raise ValueError("User not found")
    find_exercise = session.get(SessionExercise, data.session_exercise_id)  
    if not find_exercise:
        raise ValueError(f"SessionExercise with id {data.session_exercise_id} not found")

    # Create a new set entry
    new_set = WorkoutSet(
        session_exercise_id=data.session_exercise_id,
        weight=data.weight,
        reps=data.reps,
        comments=data.comments
    )
    session.add(new_set)
    session.commit()
    session.refresh(new_set)

    # Check for PR
    is_pr = check_and_create_pr(session, user_id=find_user.id, exercise_def_id=find_exercise.exercise_def_id, set_id=new_set.id, weight=new_set.weight)

    return SetResponse(
        set_id=new_set.id,
        reps=new_set.reps,
        weight=new_set.weight,
        comments=new_set.comments,
        is_pr=is_pr
    )