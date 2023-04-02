from fastapi.testclient import TestClient
from main import app
from src.objects.jwt import JWTToken
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)
jwt = JWTToken("HS256", 15)

def test01_ifTheUserLogsOutWithACorrectJwtThenTheStatusCodeIs200():
    config.setUp()
    token = jwt.create("ldefeo@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user/logout", headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheUserLogsOutWithAIncorrectJwtThenTheStatusCodeIs401():
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user/logout", headers=headers)
    assert response.status_code == 401

def test03_ifTheOrganizerLogsOutWithACorrectJwtThenTheStatusCodeIs200():
    config.setUp()
    token = jwt.create("cbravor@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/organizer/logout", headers=headers)
    config.clear()
    assert response.status_code == 200

def test04_ifTheOrganizerLogsOutWithAIncorrectJwtThenTheStatusCodeIs401():
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/organizer/logout", headers=headers)
    assert response.status_code == 401

def test05_ifTheUserLogsOutTwiceThenTheStatusCodeIs400():
    config.setUp()
    token = jwt.create("ldefeo@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.get("/user/logout", headers=headers)
    response = client.get("/user/logout", headers=headers)
    config.clear()
    assert response.status_code == 400

def test06_ifTheOrganizerLogsOutTwiceThenTheStatusCodeIs400():
    config.setUp()
    token = jwt.create("cbravor@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.get("/organizer/logout", headers=headers)
    response = client.get("/organizer/logout", headers=headers)
    config.clear()
    assert response.status_code == 400
