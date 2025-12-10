from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlmodel import Field, SQLModel, Relationship


class BackgroundProfileBase(SQLModel):
    software_experience: Optional[str] = None
    hardware_experience: Optional[str] = None
    learning_style: Optional[str] = None

class BackgroundProfileCreate(BackgroundProfileBase):
    pass

class BackgroundProfile(BackgroundProfileBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    
    user: "User" = Relationship(back_populates="background_profile")


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True)
    
class UserCreate(UserBase):
    password: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: str
    
    background_profile_id: Optional[int] = Field(default=None, foreign_key="backgroundprofile.id")
    background_profile: Optional[BackgroundProfile] = Relationship(back_populates="user")


class UserRead(UserBase):
    id: int
    background_profile_id: Optional[int]

class UserReadWithProfile(UserRead):
    background_profile: Optional[BackgroundProfile] = None
