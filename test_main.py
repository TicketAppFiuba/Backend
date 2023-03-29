from fastapi.testclient import TestClient
from main import app
from objects.jwt import JWTToken
client = TestClient(app)

jwt = JWTToken("HS256", 15)

def test_jwt_ok():
    token = jwt.create("gmovia@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/protected", headers=headers)
    assert response.status_code == 200

def test_jwt_fail():
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/protected", headers=headers)
    assert response.status_code == 401