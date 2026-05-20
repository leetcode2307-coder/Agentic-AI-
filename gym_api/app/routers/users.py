from fastapi import APIRouter,HTTPException
from app.schemas.user_schema import User,UpdateUser
from app.utils.json_handler import read_json,write_json

router = APIRouter()

FILE_PATH = "app/data/users.json"


#create user
@router.post("/")

def create_user(user: User):

    users = read_json(FILE_PATH)

    # Check duplicate email
    for existing_user in users:

        if existing_user["email"] == user.email:

            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    new_user = user.dict()

    new_user["id"] = len(users) + 1

    users.append(new_user)

    write_json(FILE_PATH, users)

    return {
        "message": "User created successfully",
        "user": new_user
    }
    
#get all users
@router.get("/")
def get_users():
    users = read_json(FILE_PATH)
    
    return users

#get one user
@router.get("/{user_id}")
def get_user(user_id: int):

    users = read_json(FILE_PATH)

    for user in users:

        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

#update user
@router.put("/{user_id}")
def update_user(user_id: int, updated_data: UpdateUser):

    users = read_json(FILE_PATH)

    for user in users:

        if user["id"] == user_id:

            update_dict = updated_data.dict(exclude_unset=True)

            user.update(update_dict)

            write_json(FILE_PATH, users)

            return {
                "message": "Profile updated",
                "user": user
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@router.delete("/{user_id}")
def delete_user(user_id: int):

    users = read_json(FILE_PATH)

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            write_json(FILE_PATH, users)

            return {
                "message": "User deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )