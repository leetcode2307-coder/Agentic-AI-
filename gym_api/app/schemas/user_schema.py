from pydantic import BaseModel  # pyright: ignore[reportMissingImports]
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: str
    weight: float
    height: float
    goal: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    goal: Optional[str] = None