from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheUserExistThenWhenTheAdmSuspendTheAccountTheStatusCodeIs200():    
    config.addUser("gmovia@fi.uba.ar")
    headers = config.addAdmin()
    response = client.post("/admin/user/suspend", params={"email": "gmovia@fi.uba.ar"}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheUserDoesntExistThenWhenTheAdmSuspendTheAccountTheStatusCodeIs400():    
    headers = config.addAdmin()
    response = client.post("/admin/user/suspend", params={"email": "gmovia@fi.uba.ar"}, headers=headers)
    assert response.status_code == 400

def test03_ifTheUserIsSuspendedThenWhenTheUserReserveAnEventTheStatusCodeIs403():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    query = {"event_id": event_id, "tickets": 2}
    headers = config.addAdmin()
    other_headers = config.addUser("rlareu@fi.uba.ar")
    client.post("/admin/user/suspend", params={"email": "rlareu@fi.uba.ar"}, headers=headers)
    response = client.post("/user/event/reservation", json=query, headers=other_headers)
    config.clear()
    assert response.status_code == 403

def test04_ifTheUserIsSuspendedAndTheAdminEnablesTheUserTheStatusCodeWillBe200():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    query = {"event_id": event_id, "tickets": 2}
    headers = config.addAdmin()
    other_headers = config.addUser("rlareu@fi.uba.ar")
    client.post("/admin/user/suspend", params={"email": "rlareu@fi.uba.ar"}, headers=headers)
    client.post("/admin/user/enable", params={"email": "rlareu@fi.uba.ar"}, headers=headers)
    response = client.post("/user/event/reservation", json=query, headers=other_headers)
    config.clear()
    assert response.status_code == 200

def test05_ifTheEventIsSuspendedThenWhenTheUserReserveAnEventTheStatusCodeIs403():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    query = {"event_id": event_id, "tickets": 2}
    headers = config.addAdmin()
    other_headers = config.addUser("rlareu@fi.uba.ar")
    client.post("/admin/event/suspend", params={"event_id": event_id}, headers=headers)
    response = client.post("/user/event/reservation", json=query, headers=other_headers)
    config.clear()
    assert response.status_code == 403

def test06_ifTheEventIsSuspendedThenWhenTheAdminEnablesTheEventTheStatusCodeIs200():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    query = {"event_id": event_id, "tickets": 2}
    headers = config.addAdmin()
    other_headers = config.addUser("rlareu@fi.uba.ar")
    client.post("/admin/event/suspend", params={"event_id": 1}, headers=headers)
    client.post("/admin/event/enable", params={"event_id": 1}, headers=headers)
    response = client.post("/user/event/reservation", json=query, headers=other_headers)
    config.clear()
    assert response.status_code == 200