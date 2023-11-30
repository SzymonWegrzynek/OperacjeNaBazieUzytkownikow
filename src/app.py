from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

app = Flask(__name__)

users = {}


@app.get("/users")
def get_users() -> Response:
    return jsonify(users, status=200)


@app.get("/users/<id>")
def get_one_user(id: str) -> Response:
    user = users.get(id)
    return jsonify(user, status=200)


@app.post("/users")
def create_user() -> Response:
    body = request.json
    users.append(body)
    return Response(status=201)


@app.patch("/users/")
def update_user() -> Response:
    return Response(status=204)


@app.delete("/users/<id>")
def delete_user(id: str) -> Response:
    if id in users:
        return Response(status=204)
    else:
        return Response(status=400)


if __name__ == "__main__":
    app.run("localhost", 8081, debug=True)
