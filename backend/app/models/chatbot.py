from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy.dialects.postgresql import JSON # For List[str] as JSON in Postgres

class Query(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    query_text: str

    response: Optional["ChatbotResponse"] = Relationship(back_populates="query")


class QueryCreate(SQLModel):
    query_text: str

class QueryRead(Query):
    pass


class ChatbotResponse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    query_id: int = Field(foreign_key="query.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    response_text: str
    source_references: Optional[List[str]] = Field(default=None, sa_column_kwargs={"type": JSON}) # Requires JSON type for list of strings

    query: Query = Relationship(back_populates="response")

class ChatbotResponseRead(ChatbotResponse):
    pass
