from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, events

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Analytics API")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(events.router, prefix="/events", tags=["Events"])

@app.get("/")
def root():
    return {"message": "API running"}