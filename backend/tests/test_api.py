from app.auth import create_access_token

def test_login_success(client, normal_user, monkeypatch):
    # mock de verificação de senha
    monkeypatch.setattr(
        "app.auth.verify_password",
        lambda plain, hashed: True,
    )

    response = client.post(
        "/token",
        data={"username": "user@test.com", "password": "1234"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_fail(client):
    response = client.post(
        "/token",
        data={"username": "inexistente@test.com", "password": "1234"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert response.status_code == 401

def test_create_user_requires_superuser(client, normal_user):
    token = create_access_token({"sub": "user@test.com"})

    response = client.post(
        "/users/",
        json={
            "name": "Novo",
            "email": "novo@test.com",
            "password": "1234",
            "is_superuser": False,
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 403

def test_create_user_ok_as_superuser(client, superuser):
    token = create_access_token({"sub": "admin@test.com"})

    response = client.post(
        "/users/",
        json={
            "name": "Novo",
            "email": "novo2@test.com",
            "password": "1234",
            "is_superuser": False,
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "novo2@test.com"

def test_list_users_requires_superuser(client, normal_user):
    token = create_access_token({"sub": "user@test.com"})

    response = client.get(
        "/users/",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 403

def test_list_users_as_superuser(client, superuser):
    token = create_access_token({"sub": "admin@test.com"})

    response = client.get(
        "/users/",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_current_user_ok(client, normal_user):
    token = create_access_token({"sub": "user@test.com"})

    response = client.get(
        "/users/me/",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json()["email"] == "user@test.com"
