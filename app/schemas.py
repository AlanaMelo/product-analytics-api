from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: str

class EventCreate(BaseModel):
    user_id: int
    event_type: str

class EventResponse(BaseModel):
    id: int
    user_id: int
    event_type: str
    timestamp: datetime

    class Config:
        from_attributes = True