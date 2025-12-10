from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Any

from agents.personalizer_agent.personalizer import BackgroundPersonalizerAgent
from backend.app.core.security import get_current_user # Assuming this function exists and returns a user object
from backend.app.models.user import User # Assuming User model is defined

router = APIRouter()

# Initialize the personalizer agent
personalizer_agent = BackgroundPersonalizerAgent()

class PersonalizationRequest(BaseModel):
    chapter_id: str
    original_content: str

class PersonalizedContentResponse(BaseModel):
    personalized_content: str

@router.post("/personalize", response_model=PersonalizedContentResponse, status_code=status.HTTP_200_OK)
async def personalize_chapter_content(
    request: PersonalizationRequest,
    current_user: User = Depends(get_current_user) # Authenticate user
):
    """
    Endpoint to personalize chapter content based on the authenticated user's background profile.
    """
    # TODO: In a real implementation, you would fetch the actual background profile
    # from the database using current_user.background_profile_id or similar.
    # For now, we'll use a mock/placeholder profile.
    mock_background_profile: Dict[str, Any] = {
        "softwareExperience": "High Python, Medium C++", # Example
        "hardwareExperience": "Low Robotics", # Example
        "learningStyle": "Visual" # Example
    }

    try:
        personalized_text = personalizer_agent.personalize_content(
            original_content=request.original_content,
            background_profile=mock_background_profile # Use actual profile data if available
        )
        return PersonalizedContentResponse(personalized_content=personalized_text)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error personalizing content: {str(e)}"
        )
