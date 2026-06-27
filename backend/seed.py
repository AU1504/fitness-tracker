from sqlmodel import Session, select
from app.database.session import engine
from app.models.exercise_definition import ExerciseDefinition
from app.models.user import User
from app.models.program import Program
from app.models.workout import Workout
from app.models.workout_exercise import WorkoutExercise


def seed_exercises(session: Session) -> dict[str, ExerciseDefinition]:
    exercises_data = [
        ("Bench Press", "Compound, Chest, Push"),
        ("Overhead Press", "Compound, Shoulders, Push"),
        ("Incline Dumbbell Press", "Compound, Chest, Push"),
        ("Tricep Pushdown", "Isolation, Triceps, Push"),
        ("Lateral Raise", "Isolation, Shoulders, Push"),
        ("Deadlift", "Compound, Back, Pull"),
        ("Pull-up", "Compound, Back, Pull"),
        ("Barbell Row", "Compound, Back, Pull"),
        ("Lat Pulldown", "Compound, Back, Pull"),
        ("Bicep Curl", "Isolation, Biceps, Pull"),
        ("Squat", "Compound, Quads, Legs"),
        ("Romanian Deadlift", "Compound, Hamstrings, Legs"),
        ("Leg Press", "Compound, Quads, Legs"),
        ("Leg Curl", "Isolation, Hamstrings, Legs"),
        ("Calf Raise", "Isolation, Calves, Legs"),
    ]

    exercise_lookup = {}

    for name, description in exercises_data:
        existing = session.exec(
            select(ExerciseDefinition).where(ExerciseDefinition.name == name)
        ).first()

        if existing:
            exercise_lookup[name] = existing
        else:
            new_exercise = ExerciseDefinition(name=name, description=description)
            session.add(new_exercise)
            session.commit()
            session.refresh(new_exercise)
            exercise_lookup[name] = new_exercise

    return exercise_lookup

def seed_user(session: Session) -> User:
    existing_user = session.exec(
        select(User).where(User.name == "testuser")
    ).first()

    if existing_user:
        return existing_user
    else:
        user = User(name="testuser")
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

def seed_program(session: Session) -> Program:
    existing_program = session.exec(
        select(Program).where(Program.name == "Test Program")
    ).first()

    if existing_program:
        return existing_program
    else:
        program = Program(
            name="Push/Pull/Legs", 
            description="A 3-day rotating split focused on puish, pull, and leg exercises."
        )
        session.add(program)
        session.commit()
        session.refresh(program)
    return program

def seed_workouts(session: Session, program: Program) -> dict[str, Workout]:
    workout_data = [
        ("Push Day", 1, "A workout focused on pushing exercises."),
        ("Pull Day", 2, "A workout focused on pulling exercises."),
        ("Leg Day", 3, "A workout focused on leg exercises.")
    ]

    workout_lookup = {}

    for name, program_day, comments in workout_data:
        existing = session.exec(
            select(Workout).where(Workout.program_day == program_day, Workout.program_id == program.id)
        ).first()

        if existing:
            workout_lookup[name] = existing
        else:
            new_workout = Workout(program_day=program_day, comments=comments, program_id=program.id)
            session.add(new_workout)
            session.commit()
            session.refresh(new_workout)
            workout_lookup[name] = new_workout  

    return workout_lookup

def seed_workout_exercises(session: Session, workouts: dict[str, Workout], exercises: dict[str, ExerciseDefinition]) -> None:
    workout_exercise_data = {
        "Push Day": [
            ("Bench Press", 1, 3, 8),
            ("Overhead Press", 2, 3, 10),
            ("Incline Dumbbell Press", 3, 3, 12),
            ("Tricep Pushdown", 4, 3, 15),
            ("Lateral Raise", 5, 3, 15)
        ],
        "Pull Day": [
            ("Deadlift", 1, 1, 5),
            ("Pull-up", 2, 3, 8),
            ("Barbell Row", 3, 3, 10),
            ("Lat Pulldown", 4, 3, 12),
            ("Bicep Curl", 5, 3, 15)
        ],
        "Leg Day": [
            ("Squat", 1, 3, 8),
            ("Romanian Deadlift", 2, 3, 10),
            ("Leg Press", 3, 3, 12),
            ("Leg Curl", 4, 3, 15),
            ("Calf Raise", 5, 4, 20)
        ]
    }

    for workout_name, exercises_list in workout_exercise_data.items():
        workout = workouts[workout_name]
        for exercise_name, exercise_order, planned_sets, planned_reps in exercises_list:
            exercise_def = exercises[exercise_name]
            existing = session.exec(
                select(WorkoutExercise).where(
                    WorkoutExercise.workout_id == workout.id,
                    WorkoutExercise.exercise_def_id == exercise_def.id
                )
            ).first()

            if not existing:
                new_workout_exercise = WorkoutExercise(
                    workout_id=workout.id,
                    exercise_order=exercise_order,
                    exercise_def_id=exercise_def.id,
                    planned_sets=planned_sets,
                    planned_reps=planned_reps
                )
                session.add(new_workout_exercise)

    session.commit()    

def run_seed():
    with Session(engine) as session:
        exercises = seed_exercises(session)
        user = seed_user(session)
        program = seed_program(session)
        workout_lookup = seed_workouts(session, program)
        seed_workout_exercises(session, workout_lookup, exercises)

    print("Seeding completed successfully.")

if __name__ == "__main__":
    run_seed()