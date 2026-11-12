import sqlite3
import pytest

import app.app as app_module
from app.app import app


# Create a fresh test database for every test
@pytest.fixture
def client(tmp_path, monkeypatch):

    db_path = tmp_path / "test_securecloud.db"

    conn = sqlite3.connect(db_path)

    conn.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

    # Make Flask use the temporary test database
    monkeypatch.setattr(
        app_module,
        "get_db_connection",
        lambda: sqlite3.connect(db_path)
    )

    return app.test_client()


# Test 1: Health endpoint
def test_health(client):

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


# Test 2: Successful registration
def test_register(client):

    response = client.post(
        "/api/users",
        json={
            "username": "testuser",
            "email": "testuser@gmail.com",
            "password": "Secure123!"
        }
    )

    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully"


# Test 3: Duplicate email
def test_duplicate_email(client):

    response1 = client.post(
        "/api/users",
        json={
            "username": "alex",
            "email": "duplicate@gmail.com",
            "password": "Secure123!"
        }
    )

    response2 = client.post(
        "/api/users",
        json={
            "username": "john",
            "email": "duplicate@gmail.com",
            "password": "Secure123!"
        }
    )

    assert response1.status_code == 201
    assert response2.status_code == 409


def test_missing_fields(client):
    response=client.post(
        "/api/users",
        json={
            "username":"alex",
            "email":"alex@gmail.com"

        }

    )

    assert response.status_code==400
    assert response.json["error"] == "All fields are required"

def test_invalid_email(client):
    response=client.post(
        "/api/users",
        json={
            
        "username": "alex",
        "email": "alexgmail.com",
        "password": "Secure123!"
    
        }
    )

    assert response.status_code==400
    assert response.json["error"]=="Invalid email"

def test_short_password(client):
    response=client.post(
        "/api/users",
        json={
                
            "username": "alex",
            "email": "alex@gmail.com",
            "password": "12345"

        }
    )

    assert response.status_code==400
    assert response.json["error"]=="Password length should be at least 8"

def test_get_users(client):

    # First register a user
    client.post(
        "/api/users",
        json={
            "username": "alex",
            "email": "alex_get@gmail.com",
            "password": "Secure123!"
        }
    )

    # Fetch users
    response = client.get("/api/users")

    assert response.status_code == 200
    assert "alex" in str(response.json)
    assert "alex_get@gmail.com" in str(response.json)

    # Ensure password is not exposed
    assert "password" not in str(response.json)
    