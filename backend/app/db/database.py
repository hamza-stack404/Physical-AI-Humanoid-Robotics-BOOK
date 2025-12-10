from sqlmodel import create_engine, Session
from backend.app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

def create_db_and_tables():
    # This will be implemented later to create tables from SQLModel metadata
    pass

def get_session():
    with Session(engine) as session:
        yield session
