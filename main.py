from flask import Flask, render_template, request, redirect, url_for, Response
from typing import Union

app = Flask(__name__)


class UserTypeModel:
    def __init__(self, firstName: str, lastName: str, birthYear: int, group: Union[str, int]):
        self.firstName = firstName
        self.lastName = lastName
        self.birthYear = birthYear
        self.group = group


@app.route('/users', methods=['GET', 'POST'])
def users() -> Union[str, Response]:
    if request.method == 'POST':
        return redirect(url_for('users'))
    else:
        return render_template('users.html')


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
