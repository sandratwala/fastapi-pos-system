from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: str
    role: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int