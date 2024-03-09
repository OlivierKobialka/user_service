from flask import Flask, Response, request, jsonify
from repositories import UserRepository
from repository_controllers import UserController

app: Flask = Flask(__name__)

# Initialize repository and controller
user_repository: UserRepository = UserRepository()
user_controller: UserController = UserController(user_repository)

# Define HTTP status codes
SUCCESS: int = 200
CREATED: int = 201
BAD_REQUEST: int = 400
NOT_FOUND: int = 404


# Routes
@app.route('/users', methods=["GET"])
def get_users():
    users = user_controller.get_all()
    return jsonify(users), SUCCESS


@app.route('/users/<int:id>', methods=["GET"])
def get_user(id):
    user = user_controller.get_by_id(id)
    if user:
        return jsonify(user), SUCCESS
    return Response("User not found", status=NOT_FOUND)


@app.route("/users", methods=["POST"])
def post_user():
    data = request.get_json()
    try:
        user_controller.create(data)
        return Response(status=CREATED)
    except (ValueError, TypeError):
        return Response("Invalid data", status=BAD_REQUEST)


@app.route("/users/<int:id>", methods=["PATCH"])
def patch_user(id):
    data = request.get_json()
    try:
        user_controller.update(id, data)
        return Response(status=NOT_FOUND)
    except (ValueError, TypeError):
        return Response("Invalid data or user not found", status=BAD_REQUEST)


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        user_controller.delete(id)
        return Response(status=NOT_FOUND)
    except ValueError:
        return Response("User not found", status=BAD_REQUEST)


if __name__ == "__main__":
    app.run(debug=True)
