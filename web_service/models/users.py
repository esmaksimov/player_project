from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
