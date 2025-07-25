from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import FormDataCreate, FormDataResponse
from database import get_db
from crud import create_form_data, get_form_data
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from config import settings

router = APIRouter(prefix="/form", tags=["form"])

bearer_scheme = HTTPBearer()
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

# Helper to verify JWT token
def verify_token(credentials: HTTPAuthorizationCredentials):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

@router.post("/submit", response_model=FormDataResponse)
def submit_form(form: FormDataCreate, db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    verify_token(credentials)
    db_form = create_form_data(db, form)
    return db_form

@router.get("/{form_id}", response_model=FormDataResponse)
def get_form(form_id: int, db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    verify_token(credentials)
    db_form = get_form_data(db, form_id)
    if not db_form:
        raise HTTPException(status_code=404, detail="Form not found")
    return db_form
