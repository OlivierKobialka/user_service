from unittest.mock import patch, Mock
import pytest
from main import app

SUCCESS: int = 200
CREATED: int = 201
BAD_REQUEST: int = 400
NOT_FOUND: int = 404
INTERNAL_SERVER_ERROR: int = 500


@pytest.fixture()
def user_data():
    return {
        "first_name": "John",
        "last_name":  "Doe",
        "age":        30
    }


@pytest.fixture()
def user():
    return {
        "id":         1,
        "first_name": "John",
        "last_name":  "Doe",
        "age":        30
    }


def test_get_users_returns_success() -> None:
    with patch('src.main.user_controller') as mock_controller:
        mock_controller.get_all.return_value = []
        with app.test_client() as client:
            response = client.get('/users')
            assert response.status_code == SUCCESS


def test_get_user_returns_success(user) -> None:
    with patch('src.main.user_controller.get_by_id') as mock_controller:
        mock_controller.return_value = user
        with app.test_client() as client:
            response = client.get('/users/1')
            assert response.status_code == SUCCESS


def test_get_user_returns_bad_request() -> None:
    with patch('src.main.user_controller.get_by_id') as mock_controller:
        mock_controller.side_effect = ValueError("User not found")
        with app.test_client() as client:
            response = client.get('/users/100')
            assert response.status_code == BAD_REQUEST


def test_post_user_returns_created(user_data) -> None:
    with patch('src.main.user_controller.create') as mock_create:
        mock_create.return_value = user_data
        with app.test_client() as client:
            response = client.post('/users', json=user_data)
            assert response.status_code == CREATED


def test_post_user_returns_bad_request() -> None:
    with patch('src.main.user_controller.create') as mock_create:
        mock_create.side_effect = ValueError("Invalid user data")
        with app.test_client() as client:
            response = client.post('/users', json={})
            assert response.status_code == BAD_REQUEST


def test_patch_user_returns_not_found(user_data) -> None:
    with patch('src.main.user_controller') as mock_update:
        mock_update.return_value = user_data
        with app.test_client() as client:
            response = client.patch('/users/1', json=user_data)
            assert response.status_code == NOT_FOUND


def test_delete_user_returns_not_found() -> None:
    with patch('src.main.user_controller.delete') as mock_delete:
        mock_delete.return_value = True
        with app.test_client() as client:
            response = client.delete('/users/1')
            assert response.status_code == NOT_FOUND


def test_delete_user_returns_bad_request() -> None:
    with patch('src.main.user_controller.delete') as mock_delete:
        mock_delete.side_effect = ValueError("User not found")
        with app.test_client() as client:
            response = client.delete('/users/100')
            assert response.status_code == BAD_REQUEST
