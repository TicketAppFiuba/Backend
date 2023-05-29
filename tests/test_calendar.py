from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheEventExistsThenWhenTheUserAddsTheEventToCalendarListTheStatusCodeWillBe200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/calendar", params=query, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheEventExistsThenWhenTheUserAddsTheEventToCalendarListTheSizeFavoriteListIs1():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "basket", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/calendar", params=query, headers=headers)
    response = client.get("/user/calendar", headers=headers)
    config.clear()
    assert response.status_code == 200
    assert len(response.json()) == 1

def test03_ifTheEventIsInTheFavoritesListThenWhenTheUserAddsTheEventToCalendarListTheStatusCodeWillBe405():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/calendar", params=query, headers=headers)
    response = client.post("/user/event/calendar", params=query, headers=headers)
    config.clear()
    assert response.status_code == 403

def test04_ifTheEventDoesntExistsThenWhenTheUserAddsTheEventToCalendarListTheStatusCodeWillBe404():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 8}
    response = client.post("/user/event/calendar", params=query, headers=headers)
    config.clear()
    assert response.status_code == 404

def test05_ifTheEventIsInFavoriteListThenWhenTheUserDeletesTheEventToCalendarListTheStatusCodeWillBe200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/calendar", params=query, headers=headers)
    response = client.delete("/user/event/calendar", params=query, headers=headers)
    config.clear()
    assert response.status_code == 200

def test06_ifTheEventIsNotInFavoriteListThenWhenTheUserDeletesTheEventToCalendarListTheStatusCodeWillBe():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.delete("/user/event/Calendar", params=query, headers=headers)
    config.clear()
    assert response.status_code == 404

def test07_ifTheEventDoesntExistThenWhenTheUserDeletesTheEventToCalendarListTheStatusCodeWillBe():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 6}
    response = client.delete("/user/event/calendar", params=query, headers=headers)
    config.clear()
    assert response.status_code == 404

def test08_ifTheEventIsNotInFavoriteListThenWhenTheUserDeletesTheEventToCalendarListTheStatusCodeWillBe():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/calendar", params=query, headers=headers)
    response = client.delete("/user/event/calendar", params=query, headers=headers)
    response = client.delete("/user/event/calendar", params=query, headers=headers)
    config.clear()
    assert response.status_code == 403

