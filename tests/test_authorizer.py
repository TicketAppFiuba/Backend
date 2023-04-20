from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheAuthorizerCanScanTheTicketThenTheStatusCodeIs200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    query = {"event_id": 1, "tickets": 3}  
    client.post("/user/event/reservation", json=query, headers=headers)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheAuthorizerCantScanTheTicketBecauseReservationDoesntExistTheStatusCodeIs403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    query = {"event_id": 1, "tickets": 3}  
    client.post("/user/event/reservation", json=query, headers=headers)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_id": 7}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    config.clear()
    assert response.status_code == 404

def test03_ifTheAuthorizerCantScanTheTicketBecauseHeDoesntHasPermissionThenTheStatusCodeIs403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)
    config.addPermissionScan("tarrachea@fi.uba.ar", 1)
    query = {"event_id": 1, "tickets": 3}  
    client.post("/user/event/reservation", json=query, headers=headers)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403
