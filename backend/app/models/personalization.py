from typing import Optional
from pydantic import BaseModel

class PersonalizedContent(BaseModel):
    personalized_content_id: Optional[str] = None  # Assuming UUID or similar for ID
    chapter_id: str
    background_profile_id: str
    personalized_text: str

    class Config:
        schema_extra = {
            "example": {
                "chapter_id": "chapter-1",
                "background_profile_id": "profile-abc",
                "personalized_text": "This is the personalized content for chapter 1."
            }
        }
