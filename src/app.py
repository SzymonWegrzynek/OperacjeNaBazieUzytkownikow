from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

app = Flask(__name__)

users = []


@app.get("/users")
def get_users() -> Response:
    return jsonify(users)
