from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Boolean, Column, DateTime, ForiegnKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
Base = declarative_base()

class user(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True, index= True)
    username = Column(String, unique= True, index= True)
    email= Column(String, unique= True, index= True)
    hashed_password= Column(String)
    is_active= Column(Boolean, default= True)
    created_at= Column(DateTime(timezone= True), server_default=func.now())

   #relationships
   tasks = relationship("task", back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key= True, index= True)
    title= Column(String, index= True)
    description= Column(String)
    completed= Column(Boolean, default=False)
    priority= Column(String, default=Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    owner_id = Column(Integer, ForiegnKey("users.id"))
    
    # Relationship
    owner = relationship("User", back_populates="tasks")
    
class UserCreate (BaseModel):
    username = str
    email = str
    password = str

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "medium"

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    priority: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
        