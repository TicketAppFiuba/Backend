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
    client.post("/event/create", json=event, headers=headers)
    get_response = client.get("/event/info", params={"event_id": 1}, headers=headers)
    assert get_response.json()["id"] == 1
    config.clear()

def test02_ifTheOrganizerCreatesAnEventWithACorrectJwtThenTheStatusCodeIs200():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
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
    response = client.post("/event/create", json=event, headers=headers)
    assert response.status_code == 200
    config.clear()

def test03_ifTheOrganizerCreatesAnEventWithAIncorrectJwtThenTheStatusCodeIs401():
    config.setUp()
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
    response = client.post("/event/create", json=event, headers=headers)
    assert response.status_code == 401
    config.clear()

def test04_ifRLareuCreatesAnEventThenTheOrganizerOfTheEventIsRLareu():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
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
    client.post("/event/create", json=event, headers=headers)
    response = client.get("/event/info", params={"event_id": 1}, headers=headers)
    assert response.json()["organizer"] == "rlareu@fi.uba.ar"
    config.clear()

def test05_ifRLareuCreatedTheEventThenRLareuCanRemoveIt():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
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
    client.post("/event/create", json=event, headers=headers)
    client.delete("/event/delete", params={"event_id": 1}, headers=headers)
    get_response = client.get("/event/info", params={"event_id": 1}, headers=headers)
    assert get_response.status_code == 404
    config.clear()

def test06_ifRLareuCreatedTheEventThenWhenRLareuRemovesTheStatusCodeIs200():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
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
    client.post("/event/create", json=event, headers=headers)
    response = client.delete("/event/delete", params={"event_id": 1}, headers=headers)
    assert response.status_code == 200
    config.clear()

def test07_ifTheEventDoesntExistThenICantRemoveIt():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/event/delete", params={"event_id": 2}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test08_ifRLareuCreatedTheEventThenCbravorCantRemoveIt():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    other_token = jwt.create("cbravor@fi.uba.ar")["access_token"]
    other_headers = {"Authorization": f"Bearer {other_token}"}
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
    client.post("/event/create", json=event, headers=headers)
    client.delete("/event/delete", params={"event_id": 1}, headers=other_headers)
    get_response = client.get("/event/info", params={"event_id": 1}, headers=headers)
    assert get_response.json()["id"] == 1
    config.clear()

def test09_ifRLareuCreatedTheEventThenWhenCBravorRemovesItTheStatusCodeIs404():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    other_token = jwt.create("cbravor@fi.uba.ar")["access_token"]
    other_headers = {"Authorization": f"Bearer {other_token}"}
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
    client.post("/event/create", json=event, headers=headers)
    response = client.delete("/event/delete", params={"event_id": 1}, headers=other_headers)
    assert response.status_code == 404
    config.clear()

def test10_ifCbravorCreatedEventThenCbravorCanModifyIt():
    config.setUp()
    token = jwt.create("cbravor@fi.uba.ar")["access_token"]
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
    client.post("/event/create", json=event, headers=headers)
    update_event = {"id": 1, "title": "string2"}
    client.put("/event/update", json=update_event, headers=headers)
    get_response = client.get("/event/info", params={"event_id": 1}, headers=headers)
    assert get_response.json()["title"] == "string2"
    config.clear()

def test11_ifCbravorCreatedEventThenCbravorModifiesTheStatusCodeIs200():
    config.setUp()
    token = jwt.create("cbravor@fi.uba.ar")["access_token"]
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
    client.post("/event/create", json=event, headers=headers)
    new_event = {"id": 1, "title": "string2"}
    response = client.put("/event/update", json=new_event, headers=headers)
    assert response.status_code == 200
    config.clear()

def test12_ifRLareuCreatedEventThenCbravorCantModifyIt():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    other_token = jwt.create("cbravor@fi.uba.ar")["access_token"]
    other_headers = {"Authorization": f"Bearer {other_token}"}
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
    client.post("/event/create", json=event, headers=headers)
    new_event = {"id": 1, "title": "string2"}
    client.put("/event/update", json=new_event, headers=other_headers)
    get_response = client.get("/event/info", params={"event_id": 1}, headers=headers)
    assert get_response.json()["title"] == "string"
    config.clear()

def test13_ifRLareuCreatedEventThenWhenCbravorModifiesTheStatusCodeItIs404():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    other_token = jwt.create("cbravor@fi.uba.ar")["access_token"]
    other_headers = {"Authorization": f"Bearer {other_token}"}
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
    client.post("/event/create", json=event, headers=headers)
    new_event = {"id": 1, "title": "string2"}
    response = client.put("/event/update", json=new_event, headers=other_headers)
    assert response.status_code == 404
    config.clear()

def test14_ifEventDoesntExistThenRLareuCantModifyIt():
    config.setUp()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    new_event = {"id": 100, "title": "string2"}
    response = client.put("/event/update", json=new_event, headers=headers)
    assert response.status_code == 404
    config.clear()