from fastapi.testclient import TestClient
from main import app
from src.objects.jwt import JWTToken
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)
jwt = JWTToken("HS256", 15)

def test01_ifTheOrganizerCreatesAnEventWithACorrectJwtThenItIsCreatedSuccessfully():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    event = {
                "title": "string",
                "category": "string",
                "images": [
                    {
                    "link": "string"
                    }
                ],
                "date": "2023-03-31",
                "description": "string",
                "tickets": 0,
                "ubication": {
                    "direction": "string",
                    "latitude": "string",
                    "length": "string"
                }
            }
    response = client.post("/event/create", json=event, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheOrganizerCreatesAnEventWithAIncorrectJwtThenTheStatusCodeIs401():
    config.setUp()
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    event = {
                "title": "string",
                "category": "string",
                "images": [
                    {
                    "link": "string"
                    }
                ],
                "date": "2023-03-31",
                "description": "string",
                "tickets": 0,
                "ubication": {
                    "direction": "string",
                    "latitude": "string",
                    "length": "string"
                }
            }
    response = client.post("/event/create", json=event, headers=headers)
    config.clear()
    assert response.status_code == 401

def test03_ifRLareuCreatesAnEventThenTheOrganizerOfTheEventIsRLareu():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    event = {
                "title": "string",
                "category": "string",
                "images": [
                    {
                    "link": "string"
                    }
                ],
                "date": "2023-03-31",
                "description": "string",
                "tickets": 0,
                "ubication": {
                    "direction": "string",
                    "latitude": "string",
                    "length": "string"
                }
            }
    response = client.post("/event/create", json=event, headers=headers)
    config.clear()
    assert response.json()["organizer_email"] == "rlareu@fi.uba.ar"
    assert response.status_code == 200

def test04_ifRLareuCreatedTheEventThenRLareuCanRemoveIt():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    event = {
                "title": "string",
                "category": "string",
                "images": [
                    {
                    "link": "string"
                    }
                ],
                "date": "2023-03-31",
                "description": "string",
                "tickets": 0,
                "ubication": {
                    "direction": "string",
                    "latitude": "string",
                    "length": "string"
                }
            }
    event_response = client.post("/event/create", json=event, headers=headers)
    event_id = event_response.json()["id"]
    response = client.delete("/event/delete", params={"event_id": event_id}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test05_ifTheEventDoesntExistThenICantRemoveIt():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/event/delete", params={"event_id": 2}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test06_ifRLareuCreatedTheEventThenCbravorCantRemoveIt():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    event = {
                "title": "string",
                "category": "string",
                "images": [
                    {
                    "link": "string"
                    }
                ],
                "date": "2023-03-31",
                "description": "string",
                "tickets": 0,
                "ubication": {
                    "direction": "string",
                    "latitude": "string",
                    "length": "string"
                }
            }
    event_response = client.post("/event/create", json=event, headers=headers)
    event_id = event_response.json()["id"]
    other_token = jwt.create("cbravor@fi.uba.ar")["access_token"]
    other_headers = {"Authorization": f"Bearer {other_token}"}
    response = client.delete("/event/delete", params={"event_id": event_id}, headers=other_headers)
    config.clear()
    assert response.status_code == 404