from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheImageIsAddedSuccessfullyThenStatusCodeIs200():    
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    response = client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheImageIsNotAddedNSuccessfullyBecauseEventNotExistThenTheStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    response = client.post("/organizer/event/images", json={"event_id": 109392, "link": "a"}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test03_ifTheImageIsUpdateSuccessfullyThenTheStatusCodeIs200():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    image = client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    response = client.put("/organizer/event/images", json={"id": image.json()["id"], "link": "b"}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test04_ifTheImageIsUpdateNotSuccessfullyBecauseImgNotExistThenTheStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    image = client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    response = client.put("/organizer/event/images", json={"id": 102300, "link": "b"}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test05_ifTheImageIsUpdateImageNotSuccessfullyBecauseImageNotExistThenTheStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    image = client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    response = client.put("/organizer/event/images", json={"id": 100, "link": "b"}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test06_ifTheImageIsDeletedSuccessfullyThenTheStatusCodeIs200():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    image = client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    response = client.delete("/organizer/event/images", json={"id": image.json()["id"]}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test07_ifTheImageIsNotDeletedSuccessfullyBecauseImgNotExistThenTheStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    response = client.delete("/organizer/event/images", json={"id": 3}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test08_ifTheImageIsNotDeletedSuccessfullyKBecauseImageNotExistThenTheStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    response = client.delete("/organizer/event/images", json={"id": 8}, headers=headers)
    config.clear()
    assert response.status_code == 404

def test09_ifTheImageIsNotUpdateSuccessfullyBecauseDoesntHasPermissionThenTheStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    other_headers = config.addOrganizer("rlareu@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")    
    image = client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    response = client.put("/organizer/event/images", json={"id": image.json()["id"], "link": "b"}, headers=other_headers)
    config.clear()
    assert response.status_code == 404

def test10_addImageOK():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    image = client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    response = client.get("/organizer/event/images", params={"event_id": event_id}, headers=headers)
    config.clear()
    assert response.json()[0]["link"] == "a"

def test11_updateImageOK():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    image = client.post("/organizer/event/images", json= {"event_id": event_id, "link": "a"}, headers=headers)
    client.put("/organizer/event/images", json={"id": image.json()["id"], "link": "b"}, headers=headers)
    response = client.get("/organizer/event/images", params={"event_id": event_id}, headers=headers)
    config.clear()
    assert response.json()[0]["link"] == "b"

def test12_deleteImageOK():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    image = client.post("/organizer/event/images", json={"event_id": event_id, "link": "a"}, headers=headers)
    client.delete("/organizer/event/images", json={"id": image.json()["id"]}, headers=headers)
    response = client.get("/organizer/event/images", params={"event_id": event_id}, headers=headers)
    config.clear()
    assert response.json() == []