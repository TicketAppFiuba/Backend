from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheEventExistThenWhenTheUserReportItTheStatusCodeShouldBe200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": event_id, "description": "str", "category": "str"}
    response = client.post("/user/event/complaint", json=query, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheEventDoesntExistThenWhenTheUserReportItTheStatusCodeShouldBe404():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 5, "description": "str", "category": "str"}
    response = client.post("/user/event/complaint", json=query, headers=headers)
    config.clear()
    assert response.status_code == 404

def test03_ifTheUserAlreadyReportedAnEventThenWhenTheUserReportItTheStatusCodeShouldBe403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": event_id, "description": "str", "category": "str"}
    client.post("/user/event/complaint", json=query, headers=headers)
    response = client.post("/user/event/complaint", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403

def test04_ifTheUserAlreadyReportedAnEventThenTheUserHasOneReport():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": event_id, "description": "str", "category": "str"}
    client.post("/user/event/complaint", json=query, headers=headers)
    response = client.get("/user/complaints", headers=headers)
    config.clear()
    assert response.status_code == 200
    assert len(response.json()) == 1

def test05_idemLastWithTwoUser():
    headers = config.addUser("rlareu@fi.uba.ar")
    otherHeaders = config.addUser("cbravor@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id_1 = config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    event_id_2 = config.addEvent("gmovia@fi.uba.ar", "soccer", "basket", 100, 100, 10, 10, "published")
    
    query = {"event_id": event_id_1, "description": "str", "category": "str"}
    otherQuery = {"event_id": event_id_2, "description": "str", "category": "str"}
    
    client.post("/user/event/complaint", json=query, headers=headers)
    client.post("/user/event/complaint", json=otherQuery, headers=headers)
    client.post("/user/event/complaint", json=otherQuery, headers=otherHeaders)
    
    response = client.get("/user/complaints", headers=headers)
    otherResponse = client.get("/user/complaints", headers=otherHeaders)
    config.clear()
    assert len(response.json()) == 2
    assert len(otherResponse.json()) == 1

def test06_userRanking():
    headers = config.addUser("rlareu@fi.uba.ar")
    otherHeaders = config.addUser("cbravor@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id_1 = config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    event_id_2 = config.addEvent("gmovia@fi.uba.ar", "soccer", "basket", 100, 100, 10, 10, "published")
    
    query = {"event_id": event_id_1, "description": "str", "category": "str"}
    otherQuery = {"event_id": event_id_2, "description": "str", "category": "str"}
    
    client.post("/user/event/complaint", json=query, headers=headers)
    client.post("/user/event/complaint", json=otherQuery, headers=headers)
    client.post("/user/event/complaint", json=otherQuery, headers=otherHeaders)
    
    headers = config.addAdmin()
    response = client.get("/admin/complaints/users/ranking", headers=headers)
    config.clear()
    assert response.json()[0]["email"] == "rlareu@fi.uba.ar"
    assert response.json()[1]["email"] == "cbravor@fi.uba.ar"

def test07_eventRanking():
    headers = config.addUser("rlareu@fi.uba.ar")
    otherHeaders = config.addUser("cbravor@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id_1 = config.addEvent("gmovia@fi.uba.ar", "e1", "c1", 100, 100, 10, 10, "published")
    event_id_2 = config.addEvent("gmovia@fi.uba.ar", "e2", "c2", 100, 100, 10, 10, "published")
    
    query = {"event_id": event_id_1, "description": "str", "category": "str"}
    otherQuery = {"event_id": event_id_2, "description": "str", "category": "str"}
    
    client.post("/user/event/complaint", json=query, headers=headers)
    client.post("/user/event/complaint", json=otherQuery, headers=headers)
    client.post("/user/event/complaint", json=otherQuery, headers=otherHeaders)
    
    headers = config.addAdmin()
    response = client.get("/admin/complaints/events/ranking", headers=headers)
    config.clear()
    assert response.json()[0]["title"] == "e2"
    assert response.json()[1]["title"] == "e1"

def test08_ifTheEventIsNotPublishedThenWhenTheUserReportItTheStatusCodeShouldBe403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "draft")
    query = {"event_id": event_id, "description": "str", "category": "str"}
    response = client.post("/user/event/complaint", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403