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
```

## Project Overview

I built a Product Analytics API using FastAPI to simulate how companies track user behavior and product performance.

The system includes user management, event tracking, and analytics metrics such as Daily Active Users and events per user.

I designed the project with a layered architecture, separating routes, services, and database logic to improve scalability and maintainability.

I also implemented proper error handling for business rules, such as preventing duplicate users and returning meaningful HTTP responses instead of server errors.

Additionally, I wrote automated tests using Pytest and handled test isolation issues by ensuring unique data during execution.

This project demonstrates my ability to combine backend engineering with product thinking and data-driven insights.