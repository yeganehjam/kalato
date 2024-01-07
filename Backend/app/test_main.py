from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from .main import app, get_db
from sql_app.database import Base
import uuid

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Define a function to create the test database
def create_test_database():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestingSessionLocal

# Override the dependency to use the test database
app.dependency_overrides[get_db] = create_test_database

# Define a fixture to clean up the test database after each test
def drop_test_database():
    Base.metadata.drop_all(bind=engine)

# Define a fixture to create a unique username
def generate_unique_username():
    return f"test_user_{uuid.uuid4().hex[:8]}"

# Define a fixture for the test client
client = TestClient(app)

def test_create_user():
    unique_username = generate_unique_username()

    response = client.post("/users/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email_address": "john@example.com",
        "phone_number": "123456789",
        "profile_picture": "url",
        "password": "password123",
        "user_type": "normal",
        "username": unique_username
    })
    assert response.status_code == 200
    assert response.json()["username"] == unique_username

def test_read_user():
    unique_username = generate_unique_username()

    # Create a test user
    create_response = client.post("/users/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email_address": "john@example.com",
        "phone_number": "123456789",
        "profile_picture": "url",
        "password": "password123",
        "user_type": "normal",
        "username": unique_username
    })
    assert create_response.status_code == 200

    # Get the user ID from the created user
    user_id = create_response.json()["id"]

    # Test reading the user
    read_response = client.get(f"/users/{user_id}")
    assert read_response.status_code == 200
    assert read_response.json()["username"] == unique_username

def test_update_user():
    unique_username = generate_unique_username()

    # Create a test user
    create_response = client.post("/users/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email_address": "john@example.com",
        "phone_number": "123456789",
        "profile_picture": "url",
        "password": "password123",
        "user_type": "normal",
        "username": unique_username
    })
    assert create_response.status_code == 200

    # Get the user ID from the created user
    user_id = create_response.json()["id"]

    # Test updating the user
    update_response = client.put(f"/users/{user_id}", json={"first_name": "Updated John"})
    assert update_response.status_code == 200
    assert update_response.json()["first_name"] == "Updated John"

def test_delete_user():
    unique_username = generate_unique_username()

    # Create a test user
    create_response = client.post("/users/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email_address": "john@example.com",
        "phone_number": "123456789",
        "profile_picture": "url",
        "password": "password123",
        "user_type": "normal",
        "username": unique_username
    })
    assert create_response.status_code == 200

    # Get the user ID from the created user
    user_id = create_response.json()["id"]

    # Test deleting the user
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["username"] == unique_username 

    # Clean up the test database after the test
    drop_test_database()
