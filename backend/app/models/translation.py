from typing import Optional
from pydantic import BaseModel

class TranslatedContent(BaseModel):
    translated_content_id: Optional[str] = None  # Assuming UUID or similar for ID
    chapter_id: str
    language_code: str # e.g., 'ur' for Urdu
    translated_text: str

    class Config:
        schema_extra = {
            "example": {
                "chapter_id": "chapter-1",
                "language_code": "ur",
                "translated_text": "یہ باب روبوٹکس کینی میٹکس پر بحث کرتا ہے۔"
            }
        }
