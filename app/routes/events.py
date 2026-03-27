from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db, event)

@router.get("/")
def list_events(db: Session = Depends(get_db)):
    return crud.get_events(db)

@router.get("/metrics/dau")
def daily_active_users(db: Session = Depends(get_db)):
    return crud.get_daily_active_users(db)