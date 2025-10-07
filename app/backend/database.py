from sqlalchemy import create_engine
from sqlalchemy.orm import sessionamaker
from .models import base 
SQLALCHEMY_DATABASE_URL = "sqlite:///./taskflow.db"

# create engine 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite specific
)
# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#helper functions 
def create_tables():
    """create databasr tables"""
    base.metadata.create_all(bind=engine)
def get_db():
    """database dependency for FastAPI"""
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
        

       


