from fastapi import APIRouter, Depends, HTTPException, status
from backend.app.models.user import UserRead, UserReadWithProfile, User, BackgroundProfileCreate, BackgroundProfile
from backend.app.core.security import get_current_user
from backend.app.db import crud # Import the crud operations
# from backend.app.api.auth import users_db, background_profiles_db # No longer needed

router = APIRouter()

@router.get("/profile", response_model=UserReadWithProfile)
async def read_user_profile(current_user: UserRead = Depends(get_current_user)):
    user_in_db = crud.get_user_by_email(current_user.email) # Fetch user from crud
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user_with_profile = UserReadWithProfile(**user_in_db.model_dump())
    if user_in_db.background_profile_id:
        profile = crud.get_background_profile_by_id(user_in_db.background_profile_id)
        if profile:
            user_with_profile.background_profile = profile
    return user_with_profile

@router.put("/profile", response_model=UserReadWithProfile)
async def update_user_profile(
    profile_update: BackgroundProfileCreate,
    current_user: UserRead = Depends(get_current_user)
):
    user_in_db = crud.get_user_by_email(current_user.email) # Fetch user from crud
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    profile: Optional[BackgroundProfile] = None
    if user_in_db.background_profile_id:
        # Update existing profile
        profile = crud.update_background_profile(user_in_db.background_profile_id, profile_update)
    else:
        # Create new profile if none exists
        profile = crud.create_background_profile(user_in_db.id, profile_update)
        user_in_db.background_profile_id = profile.id
    
    # Construct response
    user_with_profile = UserReadWithProfile(**user_in_db.model_dump())
    user_with_profile.background_profile = profile
    
    return user_with_profile

