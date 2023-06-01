from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_statistics200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    
    query = {"event_id": 1, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    
    query = {"reservation_code": reservation.json()["code"], "event_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    response = client.get("/authorizer/event/statistics", params={"event_id": 1}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_statistics200():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    query = {"event_id": 1, "tickets": 2}
    
    other_headers = config.addUser("rlareu@fi.uba.ar")
    reservation = client.post("/user/event/reservation", json=query, headers=other_headers)
    
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_code": reservation.json()["code"], "event_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)

    headers = config.addAdmin()
    response = client.get("/admin/attendances/statistics/distribution", params={"email": "rlareu@fi.uba.ar"}, headers=headers)
 
    print(response.json())
    
    response = client.get("/admin/event/statistics/state", params={"email": "rlareu@fi.uba.ar"}, headers=headers)
    print(response.json())
    config.clear()
    assert response.status_code == 200