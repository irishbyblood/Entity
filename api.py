"""
FastAPI REST API for Entity platform.
Provides endpoints for chat, memory, authentication, and more.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
import jwt
from passlib.context import CryptContext
import os

from entity import Entity, create_entity
from database import (
    get_db, init_db, User, UserProfile, Conversation, 
    KnowledgeEntry, SessionLocal
)

# Initialize FastAPI app
app = FastAPI(
    title="Entity API",
    description="Unified AI Consciousness Platform API",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

# Initialize Entity
entity_config = {
    'openai_api_key': os.getenv('OPENAI_API_KEY'),
    'anthropic_api_key': os.getenv('ANTHROPIC_API_KEY'),
    'gemini_api_key': os.getenv('GEMINI_API_KEY')
}
entity_instance = create_entity(entity_config)


# Pydantic models for API
class UserSignup(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = None


class KnowledgeAdd(BaseModel):
    title: str
    content: str
    category: Optional[str] = "general"


class Token(BaseModel):
    access_token: str
    token_type: str


# Authentication utilities
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Get the current authenticated user."""
    token = credentials.credentials
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user


# API Endpoints

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup."""
    init_db()


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Entity API",
        "version": "1.0.0",
        "description": "Unified AI Consciousness Platform",
        "status": entity_instance.get_status()
    }


@app.get("/status")
async def get_status():
    """Get Entity's current status."""
    return entity_instance.get_status()


# Authentication endpoints

@app.post("/auth/signup", response_model=Token)
async def signup(user_data: UserSignup, db: Session = Depends(get_db)):
    """Register a new user."""
    # Check if user already exists
    existing_user = db.query(User).filter(
        (User.email == user_data.email) | (User.username == user_data.username)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists"
        )
    
    # Create new user
    hashed_password = get_password_hash(user_data.password)
    new_user = User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hashed_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Create user profile
    profile = UserProfile(
        user_id=new_user.id,
        preferences={}
    )
    db.add(profile)
    db.commit()
    
    # Create access token
    access_token = create_access_token(data={"sub": new_user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/auth/login", response_model=Token)
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """Authenticate a user and return a token."""
    user = db.query(User).filter(User.email == user_data.email).first()
    
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token = create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/auth/me")
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Get current user information."""
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": current_user.username,
        "created_at": current_user.created_at.isoformat()
    }


# Chat endpoints

@app.post("/chat")
async def chat(
    message: ChatMessage,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Send a message to Entity and get a response.
    This is the main interaction endpoint.
    """
    try:
        # Process message through Entity
        response = entity_instance.think(
            user_input=message.message,
            user_id=str(current_user.id)
        )
        
        # Store conversation in database
        conversation = Conversation(
            user_id=current_user.id,
            message=message.message,
            response=response['response'],
            cortex_used=response.get('cortex'),
            session_id=message.session_id or f"session_{datetime.now().timestamp()}"
        )
        
        db.add(conversation)
        db.commit()
        
        # Extract and store any new knowledge
        await extract_and_store_knowledge(
            message.message,
            response['response'],
            current_user.id,
            db
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing message: {str(e)}"
        )


@app.get("/chat/history")
async def get_chat_history(
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get conversation history for the current user."""
    conversations = db.query(Conversation).filter(
        Conversation.user_id == current_user.id
    ).order_by(Conversation.timestamp.desc()).limit(limit).all()
    
    return [
        {
            "id": conv.id,
            "message": conv.message,
            "response": conv.response,
            "cortex": conv.cortex_used,
            "timestamp": conv.timestamp.isoformat(),
            "session_id": conv.session_id
        }
        for conv in conversations
    ]


# Knowledge/Memory endpoints

@app.post("/knowledge/add")
async def add_knowledge(
    knowledge: KnowledgeAdd,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Add a knowledge entry to Entity's memory for the user."""
    # Add to vector database
    result = entity_instance.add_knowledge(
        content=knowledge.content,
        metadata={
            "title": knowledge.title,
            "category": knowledge.category
        },
        user_id=str(current_user.id)
    )
    
    # Also store in SQL database
    entry = KnowledgeEntry(
        user_id=current_user.id,
        title=knowledge.title,
        content=knowledge.content,
        category=knowledge.category
    )
    
    db.add(entry)
    db.commit()
    db.refresh(entry)
    
    return {
        **result,
        "entry_id": entry.id
    }


@app.get("/knowledge/list")
async def list_knowledge(
    category: Optional[str] = None,
    limit: int = 50,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List knowledge entries for the current user."""
    query = db.query(KnowledgeEntry).filter(
        KnowledgeEntry.user_id == current_user.id
    )
    
    if category:
        query = query.filter(KnowledgeEntry.category == category)
    
    entries = query.order_by(KnowledgeEntry.created_at.desc()).limit(limit).all()
    
    return [
        {
            "id": entry.id,
            "title": entry.title,
            "content": entry.content,
            "category": entry.category,
            "created_at": entry.created_at.isoformat(),
            "access_count": entry.access_count
        }
        for entry in entries
    ]


@app.get("/knowledge/search")
async def search_knowledge(
    query: str,
    current_user: User = Depends(get_current_user)
):
    """Search knowledge using Entity's memory system."""
    memories = entity_instance._access_memory(
        query=query,
        user_id=str(current_user.id),
        n_results=10
    )
    
    return {
        "query": query,
        "results": memories
    }


# User profile endpoints

@app.get("/profile")
async def get_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user profile with Entity's learned information."""
    profile = db.query(UserProfile).filter(
        UserProfile.user_id == current_user.id
    ).first()
    
    if not profile:
        # Create profile if it doesn't exist
        profile = UserProfile(user_id=current_user.id, preferences={})
        db.add(profile)
        db.commit()
        db.refresh(profile)
    
    return {
        "user_id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "full_name": profile.full_name,
        "preferences": profile.preferences,
        "learned_info": profile.learned_info,
        "last_updated": profile.last_updated.isoformat() if profile.last_updated else None
    }


@app.put("/profile")
async def update_profile(
    full_name: Optional[str] = None,
    preferences: Optional[Dict] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update user profile."""
    profile = db.query(UserProfile).filter(
        UserProfile.user_id == current_user.id
    ).first()
    
    if not profile:
        profile = UserProfile(user_id=current_user.id)
        db.add(profile)
    
    if full_name is not None:
        profile.full_name = full_name
    if preferences is not None:
        profile.preferences = preferences
    
    profile.last_updated = datetime.utcnow()
    
    db.commit()
    db.refresh(profile)
    
    return {"status": "success", "message": "Profile updated"}


# Helper functions

async def extract_and_store_knowledge(
    user_message: str, 
    entity_response: str, 
    user_id: int, 
    db: Session
):
    """
    Extract important information from conversations and store it.
    This is Entity's automatic learning mechanism.
    """
    # Simple keyword-based extraction (can be enhanced with NLP)
    learning_keywords = [
        "my name is", "i am", "i like", "i prefer", "i want",
        "remember that", "don't forget", "keep in mind"
    ]
    
    user_message_lower = user_message.lower()
    
    for keyword in learning_keywords:
        if keyword in user_message_lower:
            # Store as learned information in profile
            profile = db.query(UserProfile).filter(
                UserProfile.user_id == user_id
            ).first()
            
            if profile:
                if profile.learned_info:
                    profile.learned_info += f"\n{datetime.now().strftime('%Y-%m-%d')}: {user_message}"
                else:
                    profile.learned_info = f"{datetime.now().strftime('%Y-%m-%d')}: {user_message}"
                
                profile.last_updated = datetime.utcnow()
                db.commit()
            
            break


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
