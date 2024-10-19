from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "User Service API"}

def test_create_user():
    response = client.post("/users/", json={"name": "John", "email": "john@example.com", "password": "secret"})
    assert response.status_code == 200
    assert response.json()["name"] == "John"

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
