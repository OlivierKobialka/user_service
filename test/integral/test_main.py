from main import users, by_user_id, User
import pytest

@pytest.fixture
def mock_user() -> User:
    return User(first_name="John", last_name="Doe", birth_year=1990, group="admin")


def test_get_all_users() -> None:
    all_users = users()
    assert all_users.status_code == 200
