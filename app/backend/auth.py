from datetime import datetime, timedelta, timezone
from typing import optional
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import session 
from .database import get_db
from .models import user
SECRET_KEY = "your-secret-key-here"  # Use environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer() 

def get_password_hash(password: str) -> str:
    #get hashed password 
 return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
 return pwd_context.verify(plain_password, hashed_password)

    