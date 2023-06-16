from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp
import datetime

config = TestSetUp()
client = TestClient(app)

event_json = {
    "title": "string",
    "category": "string",
    "init_date": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    "end_date": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
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
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    query = {"event_id": event_id, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheAuthorizerCantScanTheTicketBecauseReservationDoesntExistTheStatusCodeIs403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    query = {"event_id": event_id, "tickets": 3}  
    client.post("/user/event/reservation", json=query, headers=headers)
    query = {"reservation_code": 7, "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    config.clear()
    assert response.status_code == 404

def test03_ifTheAuthorizerCantScanTheTicketBecauseHeDoesntHasPermissionThenTheStatusCodeIs403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addAuthorizer("tarrachea@fi.uba.ar")
    config.addPermissionScan("tarrachea@fi.uba.ar", event_id)
    query = {"event_id": event_id, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    config.clear()
    assert response.status_code == 403

def test05_ifTheAuthorizerCantScanTheTicketBecauseDoesntPermissionTheStatusCodeIs403():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    query = {"event_id": event_id, "tickets": 3}  
    response = client.post("/user/event/reservation", json=query, headers=headers)
    query = {"reservation_code": response.json()["code"], "event_id": 2}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    config.clear()
    assert response.status_code == 404

def test06_ifTheAuthorizerCantScanTheTicketBecauseTheTicketWasAlreadyScanned():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    query = {"event_id": event_id, "tickets": 3}  
    response = client.post("/user/event/reservation", json=query, headers=headers)
    query = {"reservation_code": response.json()["code"], "event_id": event_id}
    client.post("/authorizer/ticket", json=query, headers=auth_headers)
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    config.clear()
    assert response.status_code == 403

