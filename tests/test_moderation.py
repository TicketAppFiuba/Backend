from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheUserExistThenWhenTheAdmSuspendTheAccountTheStatusCodeIs200():    
    config.addUser("gmovia@fi.uba.ar")
    response = client.post("/user/suspend", params={"email": "gmovia@fi.uba.ar"})
    config.clear()
    assert response.status_code == 200

def test02_ifTheUserDoesntExistThenWhenTheAdmSuspendTheAccountTheStatusCodeIs400():    
    response = client.post("/user/suspend", params={"email": "gmovia@fi.uba.ar"})
    assert response.status_code == 400

def test03_ifTheUserIsSuspendedThenWhenTheUserReserveAnEventTheStatusCodeIs400():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 2}
    client.post("/user/suspend", params={"email": "rlareu@fi.uba.ar"})
    response = client.post("/user/event/reservation", json=query, headers=headers)
    config.clear()
    assert response.status_code == 400