# Product Analytics API

Production-ready backend API designed to simulate how companies track user behavior and product performance.

## Features
- User management
- Event tracking
- Analytics metrics (DAU, events per user)
- Scalable backend structure

## Tech Stack
- Python
- FastAPI
- SQLAlchemy

## Architecture
This project follows a layered architecture:
- Routes (API layer)
- Services (business logic)
- Database layer

## Example Use Case
This API simulates how digital products track user behavior and generate analytics insights.

## How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload