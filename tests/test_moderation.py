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

def test03_ifTheUserIsSuspendedThenWhenTheUserReserveAnEventTheStatusCodeIs400():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    query = {"event_id": 1, "tickets": 2}
    headers = config.addAdmin()
    other_headers = config.addUser("rlareu@fi.uba.ar")
    client.post("/admin/user/suspend", params={"email": "rlareu@fi.uba.ar"}, headers=headers)
    response = client.post("/user/event/reservation", json=query, headers=other_headers)
    config.clear()
    assert response.status_code == 400