from fastapi import APIRouter, Depends, HTTPException, status
from backend.app.models.chatbot import QueryCreate, ChatbotResponseRead, Query, ChatbotResponse
from backend.app.models.user import UserRead
from backend.app.core.security import get_current_user
from backend.app.core.rag_pipeline import get_rag_response
from backend.app.db import crud

router = APIRouter()

@router.post("/query", response_model=ChatbotResponseRead)
async def chatbot_query(
    query_create: QueryCreate,
    current_user: UserRead = Depends(get_current_user)
):
    # Store the query
    new_query = crud.create_query(
        user_id=current_user.id,
        query_text=query_create.query_text
    )

    # Get RAG response
    rag_result = get_rag_response(query_create.query_text, current_user.id)
    
    # Store the response
    new_response = crud.create_chatbot_response(
        query_id=new_query.id,
        response_text=rag_result["response"],
        source_references=rag_result["source_references"]
    )
    return new_response

