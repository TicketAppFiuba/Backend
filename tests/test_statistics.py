from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheAdminGetEventsStatisticsThenTheStatusCodeIs200():
    headers = config.addUser("rlareu@fi.uba.ar")
    
    config.addOrganizer("gmovia@fi.uba.ar")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    
    event_id = config.addEvent("gmovia@fi.uba.ar", "event_1", "category_1", 100, 100, 10, 10, "published")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    
    query = {"event_id": event_id, "tickets": 3}  
    reservation = client.post("/user/event/reservation", json=query, headers=headers)
    
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)
    response = client.get("/authorizer/event/statistics", params={"event_id": event_id}, headers=auth_headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheAdminGetAttendancesDistributionTheStatusCodeIs200():
    user_headers = config.addUser("rlareu@fi.uba.ar")
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    auth_headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    
    query = {"event_id": event_id, "tickets": 2}
    
    reservation = client.post("/user/event/reservation", json=query, headers=user_headers)
    
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=auth_headers)

    headers = config.addAdmin()
    
    response = client.get("/admin/attendances/statistics/distribution", headers=headers)
    
    config.clear()
    assert response.status_code == 200

def test03_ifTheAdminGetStateStatisticsTheStatusCodeIs200():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    query = {"event_id": event_id, "tickets": 2}
    
    other_headers = config.addUser("rlareu@fi.uba.ar")
    reservation = client.post("/user/event/reservation", json=query, headers=other_headers)
    
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=headers)

    headers = config.addAdmin()
    
    response = client.get("/admin/event/statistics/state", headers=headers)

    config.clear()
    assert response.status_code == 200

def test04_ifTheAdminGetEventsDistributionTheStatusCodeIs200():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    query = {"event_id": event_id, "tickets": 2}
    
    other_headers = config.addUser("rlareu@fi.uba.ar")
    reservation = client.post("/user/event/reservation", json=query, headers=other_headers)
    
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=headers)

    headers = config.addAdmin()
    
    response = client.get("/admin/events/statistics/distribution", headers=headers)

    config.clear()
    assert response.status_code == 200

def test05_ifTheAdminGetTopOrganizersByNumberOfEventsTheStatusCodeIs200():
    config.addOrganizer("gmovia@fi.uba.ar")
    config.addOrganizer("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t1", "c", 100, 900, 7, 4, "published")
    config.addEvent("gmovia@fi.uba.ar", "t2", "c", 110, 2230, 11, 2, "published")
    config.addEvent("rlareu@fi.uba.ar", "t3", "c", 120, 115, 10, 3, "published")
    config.addEvent("gmovia@fi.uba.ar", "t4", "c", 120, 220, 10, 10, "published")
 
    headers = config.addAdmin()
    response = client.get("/admin/events/organizers/ranking", headers=headers)

    config.clear()
    assert response.status_code == 200

def test06_theTopOneIsGmoviaAndTheTopTwoIsRlareu():
    config.addOrganizer("gmovia@fi.uba.ar")
    config.addOrganizer("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t1", "c", 100, 900, 7, 4, "published")
    config.addEvent("gmovia@fi.uba.ar", "t2", "c", 110, 2230, 11, 2, "published")
    config.addEvent("rlareu@fi.uba.ar", "t3", "c", 120, 115, 10, 3, "published")
    config.addEvent("gmovia@fi.uba.ar", "t4", "c", 120, 220, 10, 10, "published")
 
    headers = config.addAdmin()
    response = client.get("/admin/events/organizers/ranking", headers=headers)

    config.clear()
    assert response.json()[0]["organizer_email"] == "gmovia@fi.uba.ar"
    assert response.json()[1]["organizer_email"] == "rlareu@fi.uba.ar"
    assert response.json()[0]["amount"] == 3
    assert response.json()[1]["amount"] == 1

def test07_theTopOneIsRlareuAndTheTopTwoIsGmovia():
    config.addOrganizer("gmovia@fi.uba.ar")
    config.addOrganizer("rlareu@fi.uba.ar")
    config.addEvent("rlareu@fi.uba.ar", "t1", "c", 100, 900, 7, 4, "published")
    config.addEvent("gmovia@fi.uba.ar", "t2", "c1", 110, 2230, 11, 2, "published")
    config.addEvent("rlareu@fi.uba.ar", "t3", "c", 120, 115, 10, 3, "published")
    config.addEvent("gmovia@fi.uba.ar", "t4", "c", 120, 220, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t3", "c1", 120, 115, 10, 3, "published")

    headers = config.addAdmin()
    response = client.get("/admin/events/organizers/ranking", params={"category": "c"}, headers=headers)

    config.clear()
    assert response.json()[0]["organizer_email"] == "rlareu@fi.uba.ar"
    assert response.json()[1]["organizer_email"] == "gmovia@fi.uba.ar"
    assert response.json()[0]["amount"] == 2
    assert response.json()[1]["amount"] == 1

def test08_ifTheAdminGetTopOrganizersByAttendancesTheStatusCodeIs200():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")

    query = {"event_id": event_id, "tickets": 2}
    other_headers = config.addUser("rlareu@fi.uba.ar")
    reservation = client.post("/user/event/reservation", json=query, headers=other_headers)
    
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=headers)

    headers = config.addAdmin()
    
    response = client.get("/admin/attendances/organizers/ranking", headers=headers)

    config.clear()
    assert response.status_code == 200

def test09_theTopOneIsGmoviaWithTwoAttendances():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t1", "c", 100, 100, 10, 10, "published")

    query = {"event_id": event_id, "tickets": 2}
    other_headers = config.addUser("rlareu@fi.uba.ar")
    reservation = client.post("/user/event/reservation", json=query, headers=other_headers)
    
    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id}
    response = client.post("/authorizer/ticket", json=query, headers=headers)

    headers = config.addAdmin()
    
    response = client.get("/admin/attendances/organizers/ranking", headers=headers)

    config.clear()
    assert response.json()[0]["organizer_email"] == "gmovia@fi.uba.ar"
    assert response.json()[0]["attendances"] == 2



def test10_theTopOneIsGmoviaWithFiveAttendances():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id_1 = config.addEvent("gmovia@fi.uba.ar", "t1", "c", 100, 100, 10, 10, "published")
    event_id_2 = config.addEvent("gmovia@fi.uba.ar", "t2", "c1", 100, 100, 10, 10, "published")

    query = {"event_id": event_id_1, "tickets": 2}
    other_headers = config.addUser("rlareu@fi.uba.ar")
    reservation = client.post("/user/event/reservation", json=query, headers=other_headers)

    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id_1)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id_1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    
    query = {"event_id": event_id_2, "tickets": 3}
    other_headers = config.addUser("cbravor@fi.uba.ar")
    reservation = client.post("/user/event/reservation", json=query, headers=other_headers)
    
    headers = config.addAuthorizer("ldefeo@fi.uba.ar")
    config.addPermissionScan("ldefeo@fi.uba.ar", event_id_2)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id_2}
    response = client.post("/authorizer/ticket", json=query, headers=headers)

    headers = config.addAdmin()
    
    response = client.get("/admin/attendances/organizers/ranking", headers=headers)

    config.clear()
    assert response.json()[0]["organizer_email"] == "gmovia@fi.uba.ar"
    assert response.json()[0]["attendances"] == 5

def test11_theTopOneIsGmoviaWithThreeAttendances():
    config.addOrganizer("gmovia@fi.uba.ar")
    event_id_1 = config.addEvent("gmovia@fi.uba.ar", "t1", "c", 100, 100, 10, 10, "published")
    event_id_2 = config.addEvent("gmovia@fi.uba.ar", "t2", "c1", 100, 100, 10, 10, "published")

    query = {"event_id": event_id_1, "tickets": 2}
    other_headers = config.addUser("rlareu@fi.uba.ar")
    reservation = client.post("/user/event/reservation", json=query, headers=other_headers)

    headers = config.addAuthorizer("cbravor@fi.uba.ar")
    config.addPermissionScan("cbravor@fi.uba.ar", event_id_1)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id_1}
    response = client.post("/authorizer/ticket", json=query, headers=headers)
    
    
    query = {"event_id": event_id_2, "tickets": 3}
    other_headers = config.addUser("cbravor@fi.uba.ar")
    reservation = client.post("/user/event/reservation", json=query, headers=other_headers)

    headers = config.addAuthorizer("ldefeo@fi.uba.ar")
    config.addPermissionScan("ldefeo@fi.uba.ar", event_id_2)
    query = {"reservation_code": reservation.json()["code"], "event_id": event_id_2}
    response = client.post("/authorizer/ticket", json=query, headers=headers)

    headers = config.addAdmin()
    
    response = client.get("/admin/attendances/organizers/ranking", params={"category": "c1"}, headers=headers)

    config.clear()
    assert response.json()[0]["organizer_email"] == "gmovia@fi.uba.ar"
    assert response.json()[0]["attendances"] == 3

def test12_ifTheAdminGetSuspensionsDistributionTheStatusCodeIs200():    
    config.addUser("gmovia@fi.uba.ar")
    headers = config.addAdmin()
    response =client.post("/admin/user/suspend", params={"email": "gmovia@fi.uba.ar"}, headers=headers)
    response = client.get("/admin/suspensions/statistics/distribution", headers=headers)
    config.clear()
    assert response.status_code == 200

def test13_ThereIsOneSuspension():    
    config.addUser("gmovia@fi.uba.ar")
    headers = config.addAdmin()
    response =client.post("/admin/user/suspend", params={"email": "gmovia@fi.uba.ar"}, headers=headers)
    response = client.get("/admin/suspensions/statistics/distribution", headers=headers)
    config.clear()
    assert response.json()[0]["suspensions"] == 1

