from fastapi import FastAPI
from app.models.exercise_definition import ExerciseDefinition
from sqlmodel import SQLModel
from app.database.session import engine
from app.routes.workout import router as workout_router


app = FastAPI()
app.include_router(workout_router)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


