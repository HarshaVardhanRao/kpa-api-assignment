from sqlalchemy.orm import Session
from models import User, FormData
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phone == phone).first()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, phone: str, password: str):
    user = get_user_by_phone(db, phone)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_form_data(db: Session, form_data):
    db_form = FormData(**form_data.dict())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form

def get_form_data(db: Session, form_id: int):
    return db.query(FormData).filter(FormData.id == form_id).first()
