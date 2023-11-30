from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

app = Flask(__name__)

users = []


@app.get("/users")
def get_users() -> Response:
    return jsonify(users, status=200)


@app.get("/users/")
def get_one_user() -> Response(status=200):
    return jsonify(users)


@app.post("/users")
def create_user() -> Response:
    body = request.json
    users.append(body)
    return Response(status=201)


@app.patch("/users/")
def update_user() -> Response:


@app.delete("/users/")
def delete_user() -> Response:
    return Response(status=204)


if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)
