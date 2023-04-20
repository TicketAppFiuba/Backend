from pydantic import BaseModel
from typing import Optional, List

class AuthorizerSchema(BaseModel):
    email: str
