from app.database.session import get_session
from app.services.pr_service import get_all_prs
from app.schemas.pr import PRResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session


router = APIRouter()

@router.get("/users/{user_id}/prs", response_model=list[PRResponse])
def get_prs(user_id: int, session: Session = Depends(get_session)):
    try:
        prs = get_all_prs(session, user_id)
        return prs
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))