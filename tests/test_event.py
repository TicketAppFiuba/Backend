from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheOrganizerCreatesAnEventWithACorrectJwtThenItIsCreatedSuccessfully():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    get_response = client.get("/event", params={"event_id": 1}, headers=headers)
    config.clear()
    assert get_response.json()["id"] == 1

def test02_ifTheOrganizerCreatesAnEventWithACorrectJwtThenTheStatusCodeIs200():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    response = client.post("/event", json=event, headers=headers)
    config.clear()
    assert response.status_code == 200

def test03_ifTheOrganizerCreatesAnEventWithAIncorrectJwtThenTheStatusCodeIs401():
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    response = client.post("/event", json=event, headers=headers)
    assert response.status_code == 401

def test04_ifRLareuCreatesAnEventThenTheOrganizerOfTheEventIsRLareu():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    response = client.get("/event", params={"event_id": 1}, headers=headers)
    config.clear()
    assert response.json()["organizer"] == "rlareu@fi.uba.ar"

def test05_ifRLareuCreatedTheEventThenRLareuCanRemoveIt():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    client.delete("/event", params={"event_id": 1}, headers=headers)
    get_response = client.get("/event", params={"event_id": 1}, headers=headers)
    config.clear()
    assert get_response.status_code == 404

def test06_ifRLareuCreatedTheEventThenWhenRLareuRemovesTheStatusCodeIs200():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    response = client.delete("/event", params={"event_id": 1}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test07_ifTheEventDoesntExistThenICantRemoveIt():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    response = client.delete("/event", params={"event_id": 2}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test08_ifRLareuCreatedTheEventThenCbravorCantRemoveIt():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    other_headers = config.setUpAccess("cbravor@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    client.delete("/event", params={"event_id": 1}, headers=other_headers)
    get_response = client.get("/event", params={"event_id": 1}, headers=headers)
    config.clear()
    assert get_response.json()["id"] == 1

def test09_ifRLareuCreatedTheEventThenWhenCBravorRemovesItTheStatusCodeIs404():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    other_headers = config.setUpAccess("cbravor@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    response = client.delete("/event", params={"event_id": 1}, headers=other_headers)
    config.clear()
    assert response.status_code == 404

def test10_ifCbravorCreatedEventThenCbravorCanModifyIt():
    headers = config.setUpAccess("cbravor@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    update_event = {"id": 1, "title": "string2"}
    client.put("/event", json=update_event, headers=headers)
    get_response = client.get("/event", params={"event_id": 1}, headers=headers)
    config.clear()
    assert get_response.json()["title"] == "string2"

def test11_ifCbravorCreatedEventThenCbravorModifiesTheStatusCodeIs200():
    headers = config.setUpAccess("cbravor@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    new_event = {"id": 1, "title": "string2"}
    response = client.put("/event", json=new_event, headers=headers)
    config.clear()
    assert response.status_code == 200

def test12_ifRLareuCreatedEventThenCbravorCantModifyIt():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    other_headers = config.setUpAccess("cbravor@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    new_event = {"id": 1, "title": "string2"}
    client.put("/event", json=new_event, headers=other_headers)
    get_response = client.get("/event", params={"event_id": 1}, headers=headers)
    config.clear()
    assert get_response.json()["title"] == "string"

def test13_ifRLareuCreatedEventThenWhenCbravorModifiesTheStatusCodeItIs404():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    other_headers = config.setUpAccess("cbravor@fi.uba.ar", "organizer")
    event = {
                "title": "string",
                "category": "string",
                "date": "2023-03-31",
                "description": "string",
                "capacity": 100,
                "vacancies": 100,
                "ubication": {
                    "direction": "string",
                    "latitude": 100,
                    "length": 100
                }
            }
    client.post("/event", json=event, headers=headers)
    new_event = {"id": 1, "title": "string2"}
    response = client.put("/event", json=new_event, headers=other_headers)
    config.clear()
    assert response.status_code == 404

def test14_ifEventDoesntExistThenRLareuCantModifyIt():
    headers = config.setUpAccess("rlareu@fi.uba.ar", "organizer")
    new_event = {"id": 100, "title": "string2"}
    response = client.put("/event", json=new_event, headers=headers)
    config.clear()
    assert response.status_code == 404