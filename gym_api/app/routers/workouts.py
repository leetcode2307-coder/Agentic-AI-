from fastapi import APIRouter
from app.schemas.workout_schema import Workout
from app.utils.json_handler import read_json, write_json

router = APIRouter()

FILE_PATH = "app/data/workouts.json"

@router.post("/")
def add_workout(workout: Workout):
    workouts = read_json(FILE_PATH)
    new_workout = workout.dict()
    new_workout["id"] = len(workouts) + 1
    workouts.append(new_workout)
    write_json(FILE_PATH, workouts)

    return {
        "message": "Workout added",
        "workout": new_workout
    }
    
@router.get("/{user_id}")
def get_user_workouts(user_id: int):
    workouts = read_json(FILE_PATH)
    user_workouts = []
    
    for workout in workouts:
        if workout["user_id"] == user_id:
            user_workouts.append(workout)

    return user_workouts
