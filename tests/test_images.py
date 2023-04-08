from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheImageIsAddedSuccessfullyThenStatusCodeIs200():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    response = client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheImageIsNotAddedNSuccessfullyBecauseEventNotExistThenTheStatusCodeIs404():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    response = client.post("/organizer/event/images", json={"event_id": 3, "link": "a"}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test03_ifTheImageIsUpdateSuccessfullyThenTheStatusCodeIs200():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.put("/organizer/event/images", json={"event_id": 1, "id": 1, "link": "b"}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test04_ifTheImageIsUpdateNotSuccessfullyBecauseImgNotExistThenTheStatusCodeIs404():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.put("/organizer/event/images", json={"event_id": 1, "id": 2, "link": "b"}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test05_ifTheImageIsUpdateImageNotSuccessfullyBecauseEventNotExistThenTheStatusCodeIs404():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.put("/organizer/event/images", json={"event_id": 3, "id": 1, "link": "b"}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test06_ifTheImageIsDeletedSuccessfullyThenTheStatusCodeIs200():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.delete("/organizer/event/images", json={"id": 1, "event_id": 1}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test07_ifTheImageIsNotDeletedSuccessfullyBecauseImgNotExistThenTheStatusCodeIs404():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.delete("/organizer/event/images", json={"id": 3, "event_id": 1}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test08_ifTheImageIsNotDeletedSuccessfullyKBecauseEventNotExistThenTheStatusCodeIs404():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.delete("/organizer/event/images", json={"id": 1, "event_id": 3}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test09_ifTheImageIsNotUpdateSuccessfullyBecauseImgDoestNotBelongToTheEventThenStatusCodeIs404():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.put("/organizer/event/images", json={"event_id": 2, "id": 1, "link": "b"}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test10_ifTheImageIsNotDeleteSuccessfullyBecauseImgDoestNotBelongToTheEventThenTheStatusCodeIs404():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.delete("/organizer/event/images", json={"id": 1, "event_id": 2}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test11_addImageOK():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.get("/organizer/event/images", params={"id": 1, "event_id": 1}, headers=headers)
    config.clear()
    assert response.json()[0]["link"] == "a"

def test12_updateImageOK():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json= {"event_id": 1, "link": "a"}, headers=headers)
    client.put("/organizer/event/images", json={"event_id": 1, "id": 1, "link": "b"}, headers=headers)
    response = client.get("/organizer/event/images", params={"id": 1, "event_id": 1}, headers=headers)
    config.clear()
    assert response.json()[0]["link"] == "b"

def test13_deleteImageOK():
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    client.post("/organizer/event/images", json={"event_id": 1, "link": "a"}, headers=headers)
    client.delete("/organizer/event/images", json={"event_id": 1, "id": 1}, headers=headers)
    response = client.get("/organizer/event/images", params={"event_id": 1, "id": 1}, headers=headers)
    config.clear()
    assert response.json() == []