from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.users import router as user_router
from app.routers.memberships import router as membership_router
from app.routers.workouts import router as workout_router
from app.routers.diets import router as diet_router

app = FastAPI(
    title="Gym Membership API"
)

app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    membership_router,
    prefix="/memberships",
    tags=["Memberships"]
)

app.include_router(
    workout_router,
    prefix="/workouts",
    tags=["Workouts"]
)

app.include_router(
    diet_router,
    prefix="/diets",
    tags=["Diets"]
)

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


@app.get("/")
def home():
    
    return {
        "message": "Gym API Running"
    }