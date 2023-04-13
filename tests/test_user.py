from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheUserConsultByBasketTitleTheAmountOfResultsIs0():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "movies", "cinema", 100, 100)
    query = {"title": "basket"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 0

def test02_ifTheUserConsultBySoccerTitleTheAmountOfResultsIs1():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "movies", "cinema", 100, 100)
    query = {"title": "soccer"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test03_ifTheUserConsultBySocTitleTheAmountOfResultsIs1():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "movies", "cinema", 100, 100)
    query = {"title": "soc"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test04_ifTheUserConsultByMusicCategoryTheAmountOfResultsIs0():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "sport", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "cinema", 100, 100)
    query = {"category": "music"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 0

def test05_ifTheUserConsultBySportCategoryTheAmountOfResultsIs1():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "sport", 100, 100)
    query = {"category": "sport"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test06_ifTheUserConsultBySporCategoryTheAmountOfResultsIs0():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "sport", 100, 100)
    query = {"category": "spor"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 0

def test07_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    query = {"latitude": 30}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["latitude"] == 100
    assert response.json()[1]["Event"]["latitude"] == 150

def test08_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    query = {"latitude": 120}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["latitude"] == 100
    assert response.json()[1]["Event"]["latitude"] == 150

def test09_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    query = {"latitude": 200}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["latitude"] == 150
    assert response.json()[1]["Event"]["latitude"] == 100

def test10_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    query = {"longitude": 100}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test11_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    query = {"longitude": 50}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test12_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    query = {"latitude": 0, "longitude": 300}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test13_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    query = {"latitude": 50, "longitude": 300}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 125
    assert response.json()[1]["Event"]["longitude"] == 100

def test14_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    query = {"latitude": 75, "longitude": 90}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test15_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    query = {"latitude": 600, "longitude": 380}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 125
    assert response.json()[1]["Event"]["longitude"] == 100

def test16_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    config.addEvent("rlareu@fi.uba.ar", "t", "c", 69, 23)
    query = {"latitude": 180, "longitude": 90}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 125
    assert response.json()[1]["Event"]["longitude"] == 100
    assert response.json()[2]["Event"]["longitude"] == 23

def test17_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125)
    config.addEvent("rlareu@fi.uba.ar", "t", "c", 69, 23)
    query = {"latitude": 23, "longitude": 51}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 23
    assert response.json()[1]["Event"]["longitude"] == 100
    assert response.json()[2]["Event"]["longitude"] == 125

def test18_addReservation():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100)
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1}
    response = client.get("/user/events", json=query, headers=headers)
    assert response.status_code == 200