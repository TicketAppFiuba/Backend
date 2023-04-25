from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)
event_json = {
    "title": "string",
    "category": "string",
    "date": "2023-03-31",
    "description": "string",
    "capacity": 100,
    "ubication": {
        "direction": "string",
        "latitude": 100,
        "longitude": 100
    },
    "agenda": [
        {
            "time": "string",
            "description": "string",
        }
    ],
    "faqs": [],
    "authorizers":[],
    "images": []
}

def test01_ifTheOrganizerCreatesAnEventWithACorrectJwtThenItIsCreatedSuccessfully():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    response = client.post("/organizer/event", json=event_json, headers=headers)
    get_response = client.get("/organizer/event", params={"event_id": response.json()["id"]}, headers=headers)
    config.clear()
    assert get_response.json()["Event"]["id"] == response.json()["id"]

def test02_ifTheOrganizerCreatesAnEventWithACorrectJwtThenTheStatusCodeIs200():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    response = client.post("/organizer/event", json=event_json, headers=headers)
    config.clear()
    assert response.status_code == 200

def test03_ifTheOrganizerCreatesAnEventWithAIncorrectJwtThenTheStatusCodeIs401():
    token = "jwt"
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/organizer/event", json=event_json, headers=headers)
    assert response.status_code == 401

def test04_ifRLareuCreatesAnEventThenTheOrganizerOfTheEventIsRLareu():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    resp = client.post("/organizer/event", json=event_json, headers=headers)
    response = client.get("/organizer/event", params={"event_id": resp.json()["id"]}, headers=headers)
    config.clear()
    assert response.json()["Event"]["organizer_email"] == "rlareu@fi.uba.ar"

def test05_ifRLareuCreatedTheEventThenRLareuCanRemoveIt():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    resp = client.post("/organizer/event", json=event_json, headers=headers)
    client.delete("/organizer/event", params={"event_id": resp.json()["id"]}, headers=headers)
    get_response = client.get("/organizer/event", params={"event_id": resp.json()["id"]}, headers=headers)
    config.clear()
    assert get_response.status_code == 404

def test06_ifRLareuCreatedTheEventThenWhenRLareuRemovesTheStatusCodeIs200():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    resp = client.post("/organizer/event", json=event_json, headers=headers)
    response = client.delete("/organizer/event", params={"event_id": resp.json()["id"]}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test07_ifTheEventDoesntExistThenICantRemoveIt():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    response = client.delete("/organizer/event", params={"event_id": 5}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test08_ifRLareuCreatedTheEventThenCbravorCantRemoveIt():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    other_headers = config.addOrganizer("cbravor@fi.uba.ar")
    resp = client.post("/organizer/event", json=event_json, headers=headers)
    client.delete("/organizer/event", params={"event_id": resp.json()["id"]}, headers=other_headers)
    get_response = client.get("/organizer/event", params={"event_id": resp.json()["id"]}, headers=headers)
    config.clear()
    assert get_response.json()["Event"]["id"] == resp.json()["id"]

def test09_ifRLareuCreatedTheEventThenWhenCBravorRemovesItTheStatusCodeIs404():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    other_headers = config.addOrganizer("cbravor@fi.uba.ar")
    resp = client.post("/organizer/event", json=event_json, headers=headers)
    response = client.delete("/organizer/event", params={"event_id": resp.json()["id"]}, headers=other_headers)
    config.clear()
    assert response.status_code == 404

def test10_ifCbravorCreatedEventThenCbravorCanModifyIt():
    headers = config.addOrganizer("cbravor@fi.uba.ar")
    resp = client.post("/organizer/event", json=event_json, headers=headers)
    update_event = {"id": resp.json()["id"], "title": "string2"}
    client.put("/organizer/event", json=update_event, headers=headers)
    get_response = client.get("/organizer/event", params={"event_id": resp.json()["id"]}, headers=headers)
    config.clear()
    assert get_response.json()["Event"]["title"] == "string2"

def test11_ifCbravorCreatedEventThenCbravorModifiesTheStatusCodeIs200():
    headers = config.addOrganizer("cbravor@fi.uba.ar")
    resp = client.post("/organizer/event", json=event_json, headers=headers)
    new_event = {"id": resp.json()["id"], "title": "string2"}
    response = client.put("/organizer/event", json=new_event, headers=headers)
    config.clear()
    assert response.status_code == 200

def test12_ifRLareuCreatedEventThenCbravorCantModifyIt():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    other_headers = config.addOrganizer("cbravor@fi.uba.ar")
    resp = client.post("/organizer/event", json=event_json, headers=headers)
    new_event = {"id": resp.json()["id"], "title": "string2"}
    client.put("/organizer/event", json=new_event, headers=other_headers)
    get_response = client.get("/organizer/event", params={"event_id": resp.json()["id"]}, headers=headers)
    config.clear()
    assert get_response.json()["Event"]["title"] == "string"

def test13_ifRLareuCreatedEventThenWhenCbravorModifiesTheStatusCodeItIs404():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    other_headers = config.addOrganizer("cbravor@fi.uba.ar")
    resp = client.post("/organizer/event", json=event_json, headers=headers)
    new_event = {"id": resp.json()["id"], "title": "string2"}
    response = client.put("/organizer/event", json=new_event, headers=other_headers)
    config.clear()
    assert response.status_code == 404

def test14_ifEventDoesntExistThenRLareuCantModifyIt():
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    new_event = {"id": 100, "title": "string2"}
    response = client.put("/organizer/event", json=new_event, headers=headers)
    config.clear()
    assert response.status_code == 404

def test15_ifTheUserCreatesAnEventThenTheCoverPicIdIsNull():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    post_response = client.post("/organizer/event", json=event_json, headers=headers)
    get_response = client.get("/organizer/event", params={"event_id": post_response.json()["id"]}, headers=headers)
    config.clear()
    assert get_response.json()["Event"]["pic_id"] == None

def test16_ifTheUserAddCoverPicThenTheCoverPicIdIsNotNull():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    post_response = client.post("/organizer/event", json=event_json, headers=headers)
    image_response = client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    client.post("/organizer/event/cover/pic", json={"id": image_response.json()["id"], "event_id": 1}, headers=headers)
    get_response = client.get("/organizer/event", params={"event_id": post_response.json()["id"]}, headers=headers)
    config.clear()
    assert get_response.json()["Event"]["pic_id"] == image_response.json()["id"]
