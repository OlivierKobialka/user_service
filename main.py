from flask import Flask, request, Response
from typing import Union, List

app = Flask(__name__)


class User:
    def __init__(self, first_name: str, last_name: str, birth_year: int, group: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.group = group

    def __repr__(self):
        return f"User(first_name='{self.first_name}', last_name='{self.last_name}', birth_year={self.birth_year}, group='{self.group}')"


all_users: List[User] = [
    User(first_name="John", last_name="Doe", birth_year=1990, group="admin"),
    User(first_name="Jane", last_name="Doe", birth_year=1991, group="user")
]


@app.route('/users', methods=['GET', 'POST'])
def users() -> Union[str, Response]:
    if request.method == 'POST':
        data = request.json
        new_user: User = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            birth_year=data['birth_year'],
            group=data['group']
        )
        all_users.append(new_user)
        return Response(str(new_user), status=201)
    elif request.method == 'GET':
        return Response(str(all_users), status=200)
    else:
        return Response("Method not allowed", status=405)


@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def by_user_id(id: int) -> Response:
    if request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        return Response(str(all_users[id]), status=200)
    else:
        return Response("Method not allowed", status=405)
