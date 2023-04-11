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