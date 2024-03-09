from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from enum import Enum


@dataclass
class AllowedGroups(Enum):
    USER = "user"
    PREMIUM = "premium"
    ADMIN = "admin"


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    birth_year: int
    group: str

    def __init__(self, user_id: int, first_name: str, last_name: str, birth_year: int,
                 group: str) -> None:
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self._group = None
        self.group = group

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        if value not in [group.value for group in AllowedGroups]:
            raise ValueError(
                f"Invalid group: {value}. Allowed values: {[group.value for group in AllowedGroups]}")
        self._group = value

    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year


class UserRepository:
    def __init__(self):
        self.users: List[User] = []
        self.last_available_id = 0

    def create(self, user_data: dict) -> User:
        user_id = self.last_available_id + 1
        user = User(
            user_id,
            user_data["first_name"],
            user_data["last_name"],
            user_data["birth_year"],
            user_data["group"]
        )
        self.users.append(user)
        return user

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update(self, user_id: int, user_data: dict) -> Optional[User]:
        user = self.get_by_id(user_id)
        if user:
            if "first_name" in user_data:
                user.first_name = user_data["first_name"]
            if "last_name" in user_data:
                user.last_name = user_data["last_name"]
            if "birth_year" in user_data:
                user.birth_year = user_data["birth_year"]
            if "group" in user_data:
                user.group = user_data["group"]
            return user
        return None

    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
