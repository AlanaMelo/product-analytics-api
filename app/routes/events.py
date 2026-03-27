from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app import services as crud
from app.database import SessionLocal

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

@router.get("/metrics/events-per-user")
def events_per_user_endpoint(db: Session = Depends(get_db)):
    return crud.events_per_user(db)