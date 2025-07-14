from pydantic import BaseModel, Field
from typing import Optional

class UserLogin(BaseModel):
    phone: str = Field(..., example="7760873976")
    password: str = Field(..., example="to_share@123")

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class FormDataBase(BaseModel):
    name: str
    email: str
    phone: str
    address: Optional[str] = None
    # Add more fields as per API spec

class FormDataCreate(FormDataBase):
    pass

class FormDataResponse(FormDataBase):
    id: int

    class Config:
        orm_mode = True
