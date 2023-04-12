from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheUserConsultByBasketTitleTheAmountOfResultsIs0():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"title": "basket"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 0

def test02_ifTheUserConsultBySoccerTitleTheAmountOfResultsIs1():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"title": "soccer"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test03_ifTheUserConsultBySocTitleTheAmountOfResultsIs1():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"title": "soc"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test04_ifTheUserConsultByMusicCategoryTheAmountOfResultsIs0():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"category": "music"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 0

def test05_ifTheUserConsultBySportCategoryTheAmountOfResultsIs1():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"category": "sport"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test06_ifTheUserConsultBySporCategoryTheAmountOfResultsIs0():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"category": "spor"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 0

def test07_():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"latitude": 30}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["latitude"] == 100
    assert response.json()[1]["Event"]["latitude"] == 150

def test08_():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"latitude": 120}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["latitude"] == 100
    assert response.json()[1]["Event"]["latitude"] == 150

def test09_():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"latitude": 200}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["latitude"] == 150
    assert response.json()[1]["Event"]["latitude"] == 100

def test10_():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"longitude": 100}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test11_():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"longitude": 50}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test12_():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"latitude": 0, "longitude": 300}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test13_():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"latitude": 50, "longitude": 300}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 125
    assert response.json()[1]["Event"]["longitude"] == 100

def test14_():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"latitude": 75, "longitude": 90}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test15_():
    config.setUpSearch()
    headers = config.setUpAccess("gmovia@fi.uba.ar", "user")
    query = {"latitude": 600, "longitude": 380}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 125
    assert response.json()[1]["Event"]["longitude"] == 100