from pydantic import BaseModel  # pyright: ignore[reportMissingImports]

class Membership(BaseModel):
    user_id: int
    membership_type: str
    duration_months: int
    price: float