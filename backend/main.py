from fastapi import FastAPI
from app.models.exercise_definition import ExerciseDefinition
from sqlmodel import SQLModel
from app.database.session import engine


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


