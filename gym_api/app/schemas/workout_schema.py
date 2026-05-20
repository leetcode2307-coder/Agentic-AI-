from pydantic import BaseModel

class Workout(BaseModel):

    user_id: int
    workout_name: str
    duration_minutes: int
    calories_burned: int