from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheEventExistsThenWhenTheUserAddsTheEventToTheFavoriteListTheStatusCodeWillBe200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/favorite", params=query, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheEventExistsThenWhenTheUserAddsTheEventToTheFavoriteListTheSizeFavoriteListIs1():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "basket", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/favorite", params=query, headers=headers)
    response = client.get("/user/favorites", headers=headers)
    config.clear()
    assert response.status_code == 200
    assert len(response.json()) == 1

def test03_ifTheEventIsInTheFavoritesListThenWhenTheUserAddsTheEventToTheFavoriteListTheStatusCodeWillBe405():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/favorite", params=query, headers=headers)
    response = client.post("/user/event/favorite", params=query, headers=headers)
    config.clear()
    assert response.status_code == 403

def test04_ifTheEventDoesntExistsThenWhenTheUserAddsTheEventToTheFavoriteListTheStatusCodeWillBe404():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 8}
    response = client.post("/user/event/favorite", params=query, headers=headers)
    config.clear()
    assert response.status_code == 404

def test05_ifTheEventIsInFavoriteListThenWhenTheUserDeletesTheEventToTheFavoriteListTheStatusCodeWillBe200():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/favorite", params=query, headers=headers)
    response = client.delete("/user/event/favorite", params=query, headers=headers)
    config.clear()
    assert response.status_code == 200

def test06_ifTheEventIsNotInFavoriteListThenWhenTheUserDeletesTheEventToTheFavoriteListTheStatusCodeWillBe():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.delete("/user/event/favorite", params=query, headers=headers)
    config.clear()
    assert response.status_code == 403

def test07_ifTheEventDoesntExistThenWhenTheUserDeletesTheEventToTheFavoriteListTheStatusCodeWillBe():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 6}
    response = client.delete("/user/event/favorite", params=query, headers=headers)
    config.clear()
    assert response.status_code == 404

def test08_ifTheEventIsNotInFavoriteListThenWhenTheUserDeletesTheEventToTheFavoriteListTheStatusCodeWillBe():
    headers = config.addUser("rlareu@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    query = {"event_id": 1}
    response = client.post("/user/event/favorite", params=query, headers=headers)
    response = client.delete("/user/event/favorite", params=query, headers=headers)
    response = client.delete("/user/event/favorite", params=query, headers=headers)
    config.clear()
    assert response.status_code == 403