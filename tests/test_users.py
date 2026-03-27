from fastapi.testclient import TestClient
from app.main import app
import uuid


client = TestClient(app)

def test_create_user():
    email = f"{uuid.uuid4()}@test.com"

    response = client.post("/users/", json={
        "name": "Test",
        "email": email
    })

    assert response.status_code == 200

def test_create_user_duplicate():
    client.post("/users/", json={
        "name": "Test",
        "email": "test@email.com"
    })

    response = client.post("/users/", json={
        "name": "Test",
        "email": "test@email.com"
    })

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already exists"