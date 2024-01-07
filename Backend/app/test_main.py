from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from .main import app, get_db
from sql_app.database import Base
import uuid
from sql_app.database import SessionLocal, engine

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Define a fixture to create a unique username and email address
def generate_unique_user():
    unique_username = f"test_user_{uuid.uuid4().hex[:8]}"
    unique_email = f"{unique_username}@example.com"
    return {"username": unique_username, "email_address": unique_email}

# Override the dependency to use the test database
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup (before test)
    create_test_database()
    yield
    # Teardown (after test)
    drop_test_database()

# Define a function to create the test database
def create_test_database():
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    Base.metadata.create_all(bind=engine)
    yield db
    db.close()

# Override the dependency to use the test database
app.dependency_overrides[get_db] = create_test_database

# Define a fixture to clean up the test database after each test
def drop_test_database():
    Base.metadata.drop_all(bind=engine)

# Define a fixture for the test client
client = TestClient(app)

def test_create_user():
    unique_user = generate_unique_user()

    response = client.post("/users/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email_address": unique_user["email_address"],
        "phone_number": "123456789",
        "profile_picture": "url",
        "password": "password123",
        "user_type": "normal",
        "username": unique_user["username"]
    })
    assert response.status_code == 200
    assert response.json()["username"] == unique_user["username"]

def test_read_user():
    unique_user = generate_unique_user()

    # Create a test user
    create_response = client.post("/users/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email_address": unique_user["email_address"],
        "phone_number": "123456789",
        "profile_picture": "url",
        "password": "password123",
        "user_type": "normal",
        "username": unique_user["username"]
    })
    assert create_response.status_code == 200

    # Test reading the user
    read_response = client.get(f"/users/{unique_user['username']}")
    assert read_response.status_code == 200 , read_response.content
    assert read_response.json()["username"] == unique_user["username"]

def test_update_user():
    unique_user = generate_unique_user()

    # Create a test user
    create_response = client.post("/users/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email_address": unique_user["email_address"],
        "phone_number": "123456789",
        "profile_picture": "url",
        "password": "password123",
        "user_type": "normal",
        "username": unique_user["username"]
    })
    assert create_response.status_code == 200

    # Test updating the user
    update_response = client.put(f"/users/{unique_user['username']}", json={"first_name": "Updated John"})
    assert update_response.status_code == 200, update_response.content
    assert update_response.json()["first_name"] == "Updated John"

def test_delete_user():
    unique_user = generate_unique_user()

    # Create a test user
    create_response = client.post("/users/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email_address": unique_user["email_address"],
        "phone_number": "123456789",
        "profile_picture": "url",
        "password": "password123",
        "user_type": "normal",
        "username": unique_user["username"]
    })
    assert create_response.status_code == 200

    # Test deleting the user
    delete_response = client.delete(f"/users/{unique_user['username']}")
    assert delete_response.status_code == 200, delete_response.content
    assert delete_response.json()["username"] == unique_user["username"]

    # Clean up the test database after the test
    drop_test_database()
