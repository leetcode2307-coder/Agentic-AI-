from app.schemas.membership_schema import Membership  # pyright: ignore[reportMissingImports]
from app.utils.json_handler import read_json,write_json
from fastapi import APIRouter

router = APIRouter()

FILE_PATH = "app/data/memberships.json"

@router.post("/")
def buy_membership(membership: Membership):
    memberships = read_json(FILE_PATH)
    new_membership = membership.dict()
    new_membership["id"] = len(memberships) + 1
    memberships.append(new_membership)
    write_json(FILE_PATH, memberships)

    return {
        "message": "Membership purchased",
        "membership": new_membership
    }
    
