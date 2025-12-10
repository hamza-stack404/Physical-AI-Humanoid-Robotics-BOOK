from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Any

from agents.translator_agent.translator import TranslatorAgent

router = APIRouter()

# Initialize the translator agent
translator_agent = TranslatorAgent()

class TranslationRequest(BaseModel):
    chapter_id: str
    original_content: str
    target_language: str

class TranslatedContentResponse(BaseModel):
    translated_content: str

@router.post("/translate", response_model=TranslatedContentResponse, status_code=status.HTTP_200_OK)
async def translate_chapter_content(
    request: TranslationRequest
):
    """
    Endpoint to translate chapter content to a target language.
    """
    try:
        translated_text = translator_agent.translate_content(
            original_content=request.original_content,
            target_language=request.target_language
        )
        return TranslatedContentResponse(translated_content=translated_text)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error translating content: {str(e)}"
        )
