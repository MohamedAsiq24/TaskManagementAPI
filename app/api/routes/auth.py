from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate,UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register",response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def register_user(user_data:UserCreate,db: Session = Depends(get_db)):
    existing_user = (db.query(User).filter(User.email == user_data.email).first())

    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Email already registered")

    user = User(email=user_data.email,hashed_password=hash_password(user_data.password))

    db.add(user)
    db.commit()
    db.refresh(user)

    return user