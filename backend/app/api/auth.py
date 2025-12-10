from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta # Added timedelta import
# from sqlmodel import Session, select # Not needed for in-memory crud
from backend.app.models.user import UserCreate, BackgroundProfileCreate, UserRead
from backend.app.core import security
from backend.app.db import crud # Import the crud operations
# from backend.app.db.database import get_session # Not needed for in-memory crud

router = APIRouter()

@router.post("/signup", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def signup_new_user(
    user_create: UserCreate, 
    background_profile_create: Optional[BackgroundProfileCreate] = None,
):
    # Check if user already exists
    if crud.get_user_by_email(user_create.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    # Hash the password
    hashed_password = security.get_password_hash(user_create.password)

    # Create user
    new_user = crud.create_user(user_create, hashed_password)

    # Create background profile if provided
    if background_profile_create:
        new_profile = crud.create_background_profile(new_user.id, background_profile_create)
        new_user.background_profile_id = new_profile.id # Update user with profile_id
    
    # In a real application, you would add user and profile to the database session and commit
    # For in-memory, changes are already reflected in crud.users_db and crud.background_profiles_db

    return new_user

@router.post("/signin")
async def signin_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = crud.get_user_by_email(form_data.username)
    if not user or not security.verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

