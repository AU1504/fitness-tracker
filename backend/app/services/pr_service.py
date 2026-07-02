from app.models.exercise_definition import ExerciseDefinition
from app.schemas.pr import PRResponse
from sqlmodel import Session, select
from app.models.pr import Pr
from app.models.user import User
from app.models.workout_set import WorkoutSet

def check_and_create_pr(session: Session, user_id: int, exercise_def_id: int, set_id: int, weight: float) -> bool:
    # Check if a PR already exists for this user and exercise definition
    existing_pr = session.exec(
        select(Pr).where(
            (Pr.user_id == user_id) & 
            (Pr.exercise_def_id == exercise_def_id)
        )
    ).first()

    if existing_pr:
        existing_set = session.get(WorkoutSet, existing_pr.set_id)
        existing_weight = existing_set.weight
    else:
        existing_weight = None  # No existing PR

    # If no existing PR or the new weight is greater than the existing PR, create a new PR
    if existing_weight is None or weight > existing_weight:
        new_pr = Pr(
            set_id=set_id,
            user_id=user_id,
            exercise_def_id=exercise_def_id
        )
        session.add(new_pr)
        session.commit()
        return True  # New PR created

    return False  # No new PR created

def get_all_prs(session: Session, user_id: int) -> list[PRResponse]:
    prs = session.exec(
        select(Pr).where(Pr.user_id == user_id)
    ).all()
    
    pr_responses = []
    for pr in prs:
        workout_set = session.get(WorkoutSet, pr.set_id)
        exercise_def = session.get(ExerciseDefinition, pr.exercise_def_id)
        pr_responses.append(PRResponse(
            exercise_name=exercise_def.name,
            pr_date=pr.date,
            pr_weight=workout_set.weight
        ))
        
    return pr_responses