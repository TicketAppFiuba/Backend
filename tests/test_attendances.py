from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_IfTheReservationExistsAndTheAuthorizerScansTheTicketToViewTheAttendeesTheStatusCodeShouldBe200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    
    query = {"event_id": event_id, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    
    response = client.get("/authorizer/event/attendances", params={"event_id": event_id}, headers=auth_headers)
    config.clear()
    assert response.status_code == 200

def test02_IfTheReservationExistsAndTheAuthorizerScansTheTicketThenWhenTheAuthorizerViewsTheAttendancesTheAttendanceCountIs1():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    
    query = {"event_id": event_id, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    
    response = client.get("/authorizer/event/attendances", params={"event_id": event_id}, headers=auth_headers)
    config.clear()
    assert len(response.json()) == 1

def test03_IfTheReservationExistsAndTheAuthorizerScansTheTicketThenWhenTheAuthorizerViewsTheAttendancesTheAttendanceCountIs1():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    event_id_1 = config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    event_id_2 = config.addEvent("gmovia@fi.uba.ar", "event_2", "category_2", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id_1)
    config.addPermissionScan("cbravor@fi.uba.ar", event_id_2)

    query = {"event_id": event_id_1, "tickets": 3}  
    client.post("/user/event/reservation", json=query, headers=headers)
    
    query = {"event_id": event_id_2, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)

    query = {"reservation_code": reservation.json()["code"], "event_id": event_id_2}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    
    response = client.get("/authorizer/event/attendances", params={"event_id": event_id_2}, headers=auth_headers)
    config.clear()
    assert len(response.json()) == 1

def test04_IfTheReservationExistsAndTheAuthorizerScansTheTicketThenWhenTheAuthorizerViewsTheAttendancesTheAttendanceCountIs1():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    event_id_1 = config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    event_id_2 = config.addEvent("gmovia@fi.uba.ar", "event_2", "category_2", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id_1)
    
    query = {"event_id": event_id_1, "tickets": 3}  
    reservation_1 = client.post("/user/event/reservation", json=query, headers=headers)
    
    query = {"event_id": event_id_2, "tickets": 3}  
    reservation_2 = client.post("/user/event/reservation", json=query, headers=headers)


    query = {"reservation_code": reservation_1.json()["code"], "event_id": event_id_1}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    
    query = {"reservation_code": reservation_2.json()["code"], "event_id": event_id_2}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)

    response = client.get("/authorizer/event/attendances", params={"event_id": event_id_1}, headers=auth_headers)
    config.clear()
    assert len(response.json()) == 1