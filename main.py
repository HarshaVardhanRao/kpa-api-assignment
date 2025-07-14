from fastapi import FastAPI
from routers import auth, form
from database import Base, engine, SessionLocal
from models import User
from passlib.context import CryptContext

app = FastAPI(title="KPA API Assignment", docs_url="/docs", redoc_url="/redoc")

app.include_router(auth.router)
app.include_router(form.router)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.phone == "7760873976").first()
        if not user:
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            hashed_password = pwd_context.hash("to_share@123")
            db_user = User(phone="7760873976", hashed_password=hashed_password)
            db.add(db_user)
            db.commit()
    finally:
        db.close()
