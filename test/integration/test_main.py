from main import app
from flask.testing import FlaskClient
import pytest

SUCCESS: int = 200
CREATED: int = 201
BAD_REQUEST: int = 400
NOT_FOUND: int = 404
INTERNAL_SERVER_ERROR: int = 500


@pytest.fixture()
def client() -> FlaskClient:
    return app.test_client()


def test_retrieve_users_success(client: FlaskClient) -> None:
    actual = client.get("/users").status_code
    assert actual == SUCCESS


def test_retrieve_user_success(client: FlaskClient) -> None:
    client.post("/users", json={
        "first_name": "John",
        "last_name":  "Doe",
        "birth_year": 1985,
        "group":      "user"
    })
    actual = client.get("/users/0").status_code
    assert actual == SUCCESS


def test_create_user_success(client: FlaskClient) -> None:
    actual = client.post("/users", json={
        "first_name": "Jane",
        "last_name":  "Smith",
        "birth_year": 1990,
        "group":      "admin"
    }).status_code
    assert actual == CREATED


def test_create_user_failure(client: FlaskClient) -> None:
    actual = client.post("/users", json={
        "last_name":  "Doe",
        "birth_year": 2000,
        "group":      "user"
    }).status_code
    assert actual == INTERNAL_SERVER_ERROR


def test_update_user_not_found(client: FlaskClient) -> None:
    actual = client.patch("/users/0", json={
        "last_name": "Johnson",
    }).status_code
    assert actual == NOT_FOUND


def test_update_user_failure(client: FlaskClient) -> None:
    actual = client.patch("/users/0", json={
        "test": "test2",
    }).status_code
    assert actual == NOT_FOUND


def test_delete_user_not_found(client: FlaskClient) -> None:
    actual = client.delete("/users/0").status_code
    assert actual == NOT_FOUND


def test_delete_user_failure(client: FlaskClient) -> None:
    actual = client.delete("/users/2").status_code
    assert actual == NOT_FOUND
