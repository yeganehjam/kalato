from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, get_db
from models import Base
import pytest

# Override database connection for testing
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Function to override the dependency to get the database session for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Test POST method for creating a user
def test_create_user():
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email_address": "john.doe@example.com",
        "phone_number": "1234567890",
        "profile_picture": "example.jpg",
        "password": "securepassword",
        "user_type": "regular",
        "username": "johndoe"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == "johndoe"

# Test GET method for reading a user
def test_read_user():
    user_id = 1  # Assuming the user with ID 1 exists
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["user_id"] == user_id

# Test PUT method for updating a user
def test_update_user():
    user_id = 1  # Assuming the user with ID 1 exists
    updated_data = {
        "first_name": "UpdatedJohn",
        "last_name": "UpdatedDoe"
    }
    response = client.put(f"/users/{user_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["first_name"] == "UpdatedJohn"
    assert response.json()["last_name"] == "UpdatedDoe"

# Test DELETE method for deleting a user
def test_delete_user():
    user_id = 1  # Assuming the user with ID 1 exists
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["user_id"] == user_id
