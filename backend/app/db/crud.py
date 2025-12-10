from typing import Optional, List, Dict, Any
from datetime import datetime
from backend.app.models.user import User, UserCreate, BackgroundProfile, BackgroundProfileCreate
from backend.app.models.chatbot import Query, QueryCreate, ChatbotResponse, ChatbotResponseRead # Import Chatbot models

# In-memory "database" for demonstration purposes
users_db: list[User] = []
background_profiles_db: list[BackgroundProfile] = []
queries_db: list[Query] = [] # New: In-memory store for queries
chatbot_responses_db: list[ChatbotResponse] = [] # New: In-memory store for responses

next_user_id = 1
next_profile_id = 1
next_query_id = 1 # New: for Query IDs
next_chatbot_response_id = 1 # New: for ChatbotResponse IDs


def create_user(user_create: UserCreate, password_hash: str) -> User:
    global next_user_id
    new_user = User(
        id=next_user_id,
        email=user_create.email,
        password_hash=password_hash,
        background_profile_id=None
    )
    next_user_id += 1
    users_db.append(new_user)
    return new_user

def get_user_by_email(email: str) -> Optional[User]:
    return next((u for u in users_db if u.email == email), None)

def create_background_profile(
    user_id: int, 
    profile_create: BackgroundProfileCreate
) -> BackgroundProfile:
    global next_profile_id
    new_profile = BackgroundProfile(
        id=next_profile_id,
        user_id=user_id,
        software_experience=profile_create.software_experience,
        hardware_experience=profile_create.hardware_experience,
        learning_style=profile_create.learning_style
    )
    next_profile_id += 1
    background_profiles_db.append(new_profile)
    return new_profile

def get_background_profile_by_id(profile_id: int) -> Optional[BackgroundProfile]:
    return next((p for p in background_profiles_db if p.id == profile_id), None)

def update_background_profile(
    profile_id: int,
    profile_update: BackgroundProfileCreate
) -> Optional[BackgroundProfile]:
    profile = get_background_profile_by_id(profile_id)
    if profile:
        for field, value in profile_update.model_dump(exclude_unset=True).items():
            setattr(profile, field, value)
    return profile

# New CRUD functions for Chatbot
def create_query(user_id: int, query_text: str) -> Query:
    global next_query_id
    new_query = Query(
        id=next_query_id,
        user_id=user_id,
        query_text=query_text,
        timestamp=datetime.utcnow() # Ensure timestamp is set
    )
    next_query_id += 1
    queries_db.append(new_query)
    return new_query

def create_chatbot_response(
    query_id: int, 
    response_text: str, 
    source_references: Optional[List[str]] = None
) -> ChatbotResponse:
    global next_chatbot_response_id
    new_response = ChatbotResponse(
        id=next_chatbot_response_id,
        query_id=query_id,
        response_text=response_text,
        source_references=source_references,
        timestamp=datetime.utcnow() # Ensure timestamp is set
    )
    next_chatbot_response_id += 1
    chatbot_responses_db.append(new_response)
    return new_response

def get_query_by_id(query_id: int) -> Optional[Query]:
    return next((q for q in queries_db if q.id == query_id), None)

def get_chatbot_response_by_query_id(query_id: int) -> Optional[ChatbotResponse]:
    return next((r for r in chatbot_responses_db if r.query_id == query_id), None)
