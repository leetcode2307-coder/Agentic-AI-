from pydantic import BaseModel

class DietPlan(BaseModel):
    goal: str
    breakfast: str
    lunch: str
    dinner: str