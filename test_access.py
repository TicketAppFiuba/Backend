from fastapi.testclient import TestClient
from main import app
from objects.jwt import JWTToken
from config.db import engine
from sqlalchemy import text

client = TestClient(app)
jwt = JWTToken("HS256", 15)

def setUp():
    with engine.connect() as c:
        c.execute(text("INSERT INTO users (username, login) VALUES ('gmovia@fi.uba.ar', 'True')"))
        c.execute(text("INSERT INTO organizers (username, login) VALUES ('cbravor@fi.uba.ar', 'True')"))

def clear():
    with engine.connect() as c:
        c.execute(text("DELETE FROM users WHERE username='gmovia@fi.uba.ar'"))
        c.execute(text("DELETE FROM organizers WHERE username='cbravor@fi.uba.ar'"))

def test_user_logout_jwt_ok():
    setUp()
    token = jwt.create("gmovia@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user/logout", headers=headers)
    clear()
    assert response.status_code == 200

def test_user_logout_jwt_fail():
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user/logout", headers=headers)
    assert response.status_code == 401

def test_organizer_logout_jwt_ok():
    setUp()
    token = jwt.create("cbravor@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/organizer/logout", headers=headers)
    clear()
    assert response.status_code == 200

def test_organizer_logout_jwt_fail():
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/organizer/logout", headers=headers)
    assert response.status_code == 401

def test_two_logout_fail():
    setUp()
    token = jwt.create("cbravor@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.get("/organizer/logout", headers=headers)
    response = client.get("/organizer/logout", headers=headers)
    clear()
    assert response.status_code == 400



