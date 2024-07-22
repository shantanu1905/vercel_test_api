import datetime
import pydantic 
from typing import List, Optional


class UserBase(pydantic.BaseModel):
    name: str
    email: str
    class Config:
       from_attributes=True

class UserCreate(UserBase):
    password: str
    class Config:
       from_attributes=True

class User(UserBase):
    id: int
    date_created: datetime.datetime
    class Config:
       from_attributes=True


class GenerateUserToken(pydantic.BaseModel):
    username: str
    password: str
    class Config:
        from_attributes=True

class GenerateOtp(pydantic.BaseModel):
    email: str
    
class VerifyOtp(pydantic.BaseModel):
    email: str
    otp: int


