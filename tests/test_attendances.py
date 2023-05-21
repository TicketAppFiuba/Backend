from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_IfTheReservationExistsAndTheAuthorizerScansTheTicketToViewTheAttendeesTheStatusCodeShouldBe200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    
    query = {"event_id": 1, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_code": reservation.json()["code"], "event_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    
    response = client.get("/authorizer/event/attendances", params={"event_id": 1}, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_IfTheReservationExistsAndTheAuthorizerScansTheTicketThenWhenTheAuthorizerViewsTheAttendancesTheAttendanceCountIs1():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    
    query = {"event_id": 1, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_code": reservation.json()["code"], "event_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    
    response = client.get("/authorizer/event/attendances", params={"event_id": 1}, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test03_IfTheReservationExistsAndTheAuthorizerScansTheTicketThenWhenTheAuthorizerViewsTheAttendancesTheAttendanceCountIs1():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "event_2", "category_2", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    config.addPermissionScan("cbravor@fi.uba.ar", 2)


    query = {"event_id": 1, "tickets": 3}  
    client.post("/user/event/reservation", json=query, headers=headers)
    
    query = {"event_id": 2, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)

    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_code": reservation.json()["code"], "event_id": 2}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    
    response = client.get("/authorizer/event/attendances", params={"event_id": 2}, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test04_IfTheReservationExistsAndTheAuthorizerScansTheTicketThenWhenTheAuthorizerViewsTheAttendancesTheAttendanceCountIs1():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "event_2", "category_2", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    
    query = {"event_id": 1, "tickets": 3}  
    reservation_1 = client.post("/user/event/reservation", json=query, headers=headers)
    
    query = {"event_id": 2, "tickets": 3}  
    reservation_2 = client.post("/user/event/reservation", json=query, headers=headers)

    headers = config.addAuthorizer("cbravor@fi.uba.ar")

    query = {"reservation_code": reservation_1.json()["code"], "event_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    
    query = {"reservation_code": reservation_2.json()["code"], "event_id": 2}
    response = client.post("/authorizer/ticket", json=query, headers=headers)

    response = client.get("/authorizer/event/attendances", params={"event_id": 1}, headers=headers)
    config.clear()
    assert len(response.json()) == 1
