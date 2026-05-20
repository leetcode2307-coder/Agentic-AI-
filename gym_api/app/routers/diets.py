from fastapi import APIRouter
from app.schemas.diet_schema import DietPlan
from app.utils.json_handler import read_json, write_json

router = APIRouter()

FILE_PATH = "app/data/diets.json"

@router.post("/")
def create_diet_plan(plan: DietPlan):
    diets = read_json(FILE_PATH)
    new_plan = plan.dict()
    new_plan["id"] = len(diets) + 1
    diets.append(new_plan)
    write_json(FILE_PATH, diets)

    return {
        "message": "Diet plan added",
        "diet_plan": new_plan
    }
    
@router.get("/")
def get_diet_plans():
    diets = read_json(FILE_PATH)

    return diets