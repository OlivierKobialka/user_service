from flask import Flask, request, Response
from typing import Union, List

app = Flask(__name__)


class User:
    def __init__(self, firstName: str, lastName: str, birthYear: int, group: str):
        self.firstName = firstName
        self.lastName = lastName
        self.birthYear = birthYear
        self.group = group

    def __repr__(self):
        return f"User(firstName='{self.firstName}', lastName='{self.lastName}', birthYear={self.birthYear}, group='{self.group}')"


all_users: List[User] = [
    User(firstName="John", lastName="Doe", birthYear=1990, group="admin"),
    User(firstName="Jane", lastName="Doe", birthYear=1991, group="user")
]


@app.route('/users', methods=['GET', 'POST'])
def users() -> Union[str, Response]:
    if request.method == 'POST':
        return "POST"
    elif request.method == 'GET':
        pass
    else:
        return Response("Method not allowed", status=405)


@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def by_user_id(id: int) -> Response:
    if request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        pass
    else:
        return Response("Method not allowed", status=405)
