from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheUserLogsOutWithACorrectJwtThenTheStatusCodeIs200():
    headers = config.addUser("ldefeo@fi.uba.ar")
    response = client.get("/user/logout", headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheUserLogsOutWithAIncorrectJwtThenTheStatusCodeIs401():
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/user/logout", headers=headers)
    assert response.status_code == 401

def test03_ifTheOrganizerLogsOutWithACorrectJwtThenTheStatusCodeIs200():
    headers = config.addOrganizer("ldefeo@fi.uba.ar")
    response = client.get("/organizer/logout", headers=headers)
    config.clear()
    assert response.status_code == 200

def test04_ifTheOrganizerLogsOutWithAIncorrectJwtThenTheStatusCodeIs401():
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/organizer/logout", headers=headers)
    assert response.status_code == 401

def test05_ifTheUserLogsOutTwiceThenTheStatusCodeIs400():
    headers = config.addUser("ldefeo@fi.uba.ar")
    client.get("/user/logout", headers=headers)
    response = client.get("/user/logout", headers=headers)
    config.clear()
    assert response.status_code == 400

def test06_ifTheOrganizerLogsOutTwiceThenTheStatusCodeIs400():
    headers = config.addOrganizer("ldefeo@fi.uba.ar")
    client.get("/organizer/logout", headers=headers)
    response = client.get("/organizer/logout", headers=headers)
    config.clear()
    assert response.status_code == 400
