from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import func
from app.models import Event


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(
        user_id=event.user_id,
        event_type=event.event_type
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_events(db: Session):
    return db.query(models.Event).all()

def get_daily_active_users(db):
    results = db.query(
        func.date(Event.timestamp),
        func.count(Event.user_id.distinct())
    ).group_by(func.date(Event.timestamp)).all()

    # Converter para JSON
    return [
        {
            "date": str(row[0]),
            "active_users": row[1]
        }
        for row in results
    ]

def events_per_user(db):
    results = db.query(
        Event.user_id,
        func.count(Event.id)
    ).group_by(Event.user_id).all()

    return [
        {
            "user_id": row[0],
            "event_count": row[1]
        }
        for row in results
    ]