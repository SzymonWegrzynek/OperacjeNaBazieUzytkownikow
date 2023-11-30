from src.app import app

STATUS_OK = 200
CREATE = 204


def test_ping_endpoint() -> None:
    client = app.test_client()
    actual = client.get("/ping")
    assert actual.status_code == STATUS_OK


def test_create_user_endpoint() -> None:
    client = app.test_client()
    actual = client.post("/users")
    assert actual.status_code == CREATE
