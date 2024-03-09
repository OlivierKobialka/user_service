from repositories import UserRepository
from typing import Optional, List
from dataclasses import asdict


def _as_dict_safe(obj) -> Optional[dict]:
    try:
        return asdict(obj)
    except AttributeError:
        return None


class UserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def create(self, user_data: dict) -> dict:
        user = self._repository.create(user_data)
        return _as_dict_safe(user)

    def get_all(self) -> List[dict]:
        users = self._repository.get_all()
        return [_as_dict_safe(user) for user in users]

    def get_by_id(self, user_id: int) -> Optional[dict]:
        user = self._repository.get_by_id(user_id)
        return _as_dict_safe(user) if user is not None else None

    def update(self, user_id: int, user_data: dict) -> Optional[dict]:
        user = self._repository.update(user_id, user_data)
        return _as_dict_safe(user) if user is not None else None

    def delete(self, user_id: int) -> bool:
        return self._repository.delete(user_id)
