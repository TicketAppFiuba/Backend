from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp
import datetime

config = TestSetUp()
client = TestClient(app)

event_json = {
    "title": "string",
    "category": "string",
    "date": '2023-05-12T12:30:45',
    "description": "string",
    "capacity": 100,
    "ubication": {
        "direction": "string",
        "latitude": 100,
        "longitude": 100
    },
    "state": "published",
    "agenda": [
        {
            "time": "string",
            "description": "string",
        }
    ],
    "faqs": [
        {
        "question": "string",
        "response": "string"
        }
    ],
    "authorizers": [
        {
        "email": "string"
        }
    ],
    "images": [
        {
        "link": "string"
        }
    ]
}

def test01_ifTheAuthorizerCanScanTheTicketThenTheStatusCodeIs200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    query = {"event_id": 1, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_code": reservation.json()["code"], "event_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheAuthorizerCantScanTheTicketBecauseReservationDoesntExistTheStatusCodeIs403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    query = {"event_id": 1, "tickets": 3}  
    client.post("/user/event/reservation", json=query, headers=headers)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_code": 7, "event_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    config.clear()
    assert response.status_code == 404

def test03_ifTheAuthorizerCantScanTheTicketBecauseHeDoesntHasPermissionThenTheStatusCodeIs403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addPermissionScan("tarrachea@fi.uba.ar", 1)
    query = {"event_id": 1, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_code": reservation.json()["code"], "event_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403
    
def test04_ifTheAuthorizerCanScanTheTicketThenTheStatusCodeIs200():
    org_headers = config.addOrganizer("rlareu@fi.uba.ar")
    client.post("/organizer/event", json=event_json, headers=org_headers)
    headers = config.addUser("gmovia@fi.uba.ar")
    query = {"event_id": 1, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    auth_headers = config.addAuthorizer("rlareu@fi.uba.ar")
    query = {"reservation_code": reservation.json()["code"], "event_id": 1}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    config.clear()
    assert response.status_code == 200

def test05_ifTheAuthorizerCantScanTheTicketBecauseDoesntPermissionTheStatusCodeIs403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    query = {"event_id": 1, "tickets": 3}  
    response = client.post("/user/event/reservation", json=query, headers=headers)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_code": response.json()["code"], "event_id": 2}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403

def test06_ifTheAuthorizerCantScanTheTicketBecauseTheTicketWasAlreadyScanned():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", 1)
    query = {"event_id": 1, "tickets": 3}  
    response = client.post("/user/event/reservation", json=query, headers=headers)
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    query = {"reservation_code": response.json()["code"], "event_id": 2}
    client.post("/authorizer/ticket", json=query, headers=headers)
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403