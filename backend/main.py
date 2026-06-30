from fastapi import FastAPI
from app.models.exercise_definition import ExerciseDefinition
from sqlmodel import SQLModel
from app.database.session import engine
from app.routes.workout import router as workout_router
from app.routes.session import router as session_router


app = FastAPI()
app.include_router(workout_router)
app.include_router(session_router)  # Include the session router

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


