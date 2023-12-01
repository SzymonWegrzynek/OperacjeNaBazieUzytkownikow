from src.app import app

STATUS_OK = 200
CREATE = 204


def test_users_endpoint() -> None:
    client = app.test_client()
    actual = client.get("/users")
    assert actual.status_code == STATUS_OK


def test_get_one_user_endpoint() -> None:
    client = app.test_client()
    actual = client.get("/users/1")
    assert actual.status_code == STATUS_OK


def test_create_user_endpoint() -> None:
    client = app.test_client()
    actual = client.post("/users")
    assert actual.status_code == CREATE


def test_patch_user_endpoint(status_code=None) -> None:
    data = {'id': 1, 'name': 'Updated Name'}
    response_patch = app.patch('/users', json=data)
    assert (response_patch, status_code == 204)


def test_put_user_endpoint(status_code=None) -> None:
    data = {'id': 1, 'name': 'Replaced Name'}
    response_put = app.put('/users/1', json=data)
    assert (response_put, status_code == 204)


def test_delete_user_endpoint(status_code=None) -> None:
    data = app.delete('/users/1')
    assert (data, status_code == 204)
