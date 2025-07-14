
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from schemas import UserLogin, Token
from database import get_db
from crud import authenticate_user, get_user_by_phone
from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime
from config import settings

router = APIRouter(prefix="/auth", tags=["auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRegister(UserLogin):
    pass

@router.post("/register", status_code=201)
def register(user: UserRegister = Body(...), db: Session = Depends(get_db)):
    existing = get_user_by_phone(db, user.phone)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = pwd_context.hash(user.password)
    from models import User
    db_user = User(phone=user.phone, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "phone": db_user.phone}

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

@router.post("/login", response_model=Token)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_login.phone, user_login.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user.phone, "exp": datetime.utcnow() + access_token_expires}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": encoded_jwt, "token_type": "bearer"}
