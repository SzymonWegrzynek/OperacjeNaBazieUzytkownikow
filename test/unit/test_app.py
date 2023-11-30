from src.app import app
from src.app import create_user
from src.app import users


def test_create_user() -> None:
    payload = {
        "name": "John",
        "lastname": "Doe"
    }
    with app.test_request_context(json=payload):
        actual = create_user()
    assert payload in users


def test_returns_400_on_bad_request() -> None:
    payload = {
        "xyz": "abc"
    }
    with app.test_request_context(json=payload):
        actual = create_user()
    assert actual.status_code == 400
