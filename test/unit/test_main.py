import pytest
from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert b"John" in response.data
    assert b"Jane" in response.data


def test_post_user(client):
    new_user = {
        "first_name": "Alice",
        "last_name":  "Wonderland",
        "birth_year": 1995,
        "group":      "user"
    }
    response = client.post('/users', json=new_user)
    assert response.status_code == 201
    assert b"Alice" in response.data


def test_get_user_by_id(client):
    response = client.get('/users/0')
    assert response.status_code == 200
    assert b"John" in response.data


def test_patch_user_by_id(client):
    updated_user = {
        "first_name": "Updated",
        "last_name":  "User",
        "birth_year": 1990,
        "group":      "admin"
    }
    response = client.patch('/users/0', json=updated_user)
    assert response.status_code == 200
    assert b"Updated" in response.data


def test_delete_user_by_id(client):
    response = client.delete('/users/0')
    assert response.status_code == 200
    assert b"User deleted" in response.data
    response = client.get('/users')
    assert b"John" not in response.data
