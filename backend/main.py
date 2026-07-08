from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.exercise_definition import ExerciseDefinition
from sqlmodel import SQLModel
from app.database.session import engine
from app.routes.workout import router as workout_router
from app.routes.session import router as session_router
from app.routes.set import router as set_router
from app.routes.pr import router as pr_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(workout_router)
app.include_router(session_router)  # Include the session router
app.include_router(set_router)  # Include the set router
app.include_router(pr_router)  # Include the PR router

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


