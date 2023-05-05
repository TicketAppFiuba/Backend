from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheUserConsultByBasketTitleTheAmountOfResultsIs0():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "movies", "cinema", 100, 100, 10, 10, "published")
    query = {"title": "basket"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 0

def test02_ifTheUserConsultBySoccerTitleTheAmountOfResultsIs1():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "movies", "cinema", 100, 100, 10, 10, "published")
    query = {"title": "soccer"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test03_ifTheUserConsultBySocTitleTheAmountOfResultsIs1():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "movies", "cinema", 100, 100, 10, 10, "published")
    query = {"title": "soc"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test04_ifTheUserConsultByMusicCategoryTheAmountOfResultsIs0():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "sport", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "cinema", 100, 100, 10, 10, "published")
    query = {"category": "music"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 0

def test05_ifTheUserConsultBySportCategoryTheAmountOfResultsIs1():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "sport", 100, 100, 10, 10, "published")
    query = {"category": "sport"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test06_ifTheUserConsultBySporCategoryTheAmountOfResultsIs0():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "sport", 100, 100, 10, 10, "published")
    query = {"category": "spor"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 0

def test07_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    query = {"latitude": 30}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["latitude"] == 100
    assert response.json()[1]["Event"]["latitude"] == 150

def test08_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    query = {"latitude": 120}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["latitude"] == 100
    assert response.json()[1]["Event"]["latitude"] == 150

def test09_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    query = {"latitude": 200}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["latitude"] == 150
    assert response.json()[1]["Event"]["latitude"] == 100

def test10_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    query = {"longitude": 100}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test11_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    query = {"longitude": 50}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test12_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    query = {"latitude": 0, "longitude": 300}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test13_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    query = {"latitude": 50, "longitude": 300}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 125
    assert response.json()[1]["Event"]["longitude"] == 100

def test14_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    query = {"latitude": 75, "longitude": 90}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test15_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    query = {"latitude": 600, "longitude": 380}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 125
    assert response.json()[1]["Event"]["longitude"] == 100

def test16_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    config.addEvent("rlareu@fi.uba.ar", "t", "c", 69, 23, 10, 10, "published")
    query = {"latitude": 180, "longitude": 90}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 125
    assert response.json()[1]["Event"]["longitude"] == 100
    assert response.json()[2]["Event"]["longitude"] == 23

def test17_calculateDistance():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    config.addEvent("rlareu@fi.uba.ar", "t", "c", 69, 23, 10, 10, "published")
    query = {"latitude": 23, "longitude": 51}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 23
    assert response.json()[1]["Event"]["longitude"] == 100
    assert response.json()[2]["Event"]["longitude"] == 125

def test18_ifTheUserDoesntHaveAReservationForTheEventThenWhenHeReservesAnEventThenTheStatusCodeWillBe200():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 2}
    response = client.post("/user/event/reservation", json=query, headers=headers)
    config.clear()
    assert response.status_code == 200

def test19_ifTheEventDoesntExistThenWhenHeReservesAnEventThenTheStatusCodeWillBe404():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 5, "tickets": 3}
    response = client.post("/user/event/reservation", json=query, headers=headers)
    config.clear()
    assert response.status_code == 404 

def test20_ifTheUserHaveAReservationForTheEventThenWhenHeReservesAnEventThenTheStatusCodeWillBe403():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 1}
    client.post("/user/event/reservation", json=query, headers=headers)
    response = client.post("/user/event/reservation", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403

def test21_ifTheUserDoesntHaveAReservationForTheEventThenWhenHeReservesFiveEventTicketsThenTheStatusCodeWillBe403():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 5}
    response = client.post("/user/event/reservation", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403

def test22_ifTheNumberOfVacanciesIs2ForTheEventThenWhenHeReservesThreeEventTicketsThenTheStatusCodeWillBe403():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 2, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 3}
    response = client.post("/user/event/reservation", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403

def test23_ifTheUserDoesntHaveAReservationForTheEventThenWhenHeReservesThreeEventTicketsThenTheVacanciesWillBe7():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 3}
    client.post("/user/event/reservation", json=query, headers=headers)
    response = client.get("/user/event", params={"event_id": 1}, headers=headers)
    config.clear()
    assert response.json()["Event"]["vacancies"] == 7

def test24_fTheEventHasOnlyTwoAvailableVacanciesAndTheUserReservesThreeEventTicketTheVacanciesWillBeTwo():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 2, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 3}
    client.post("/user/event/reservation", json=query, headers=headers)
    response = client.get("/user/event", params={"event_id": 1}, headers=headers)
    config.clear()
    assert response.json()["Event"]["vacancies"] == 2

def test25_ifTheEventHasOnlyTwoAvailableVacanciesAndTHeUserReservesZeroEventTicketTheStatusCodeWillBe403():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 2, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 0}
    response = client.post("/user/event/reservation", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403

def test26_ifTheUserReservesTwoEventsThenTheNumberOfReservesIsTwo():
    config.addEvent("cbravor@fi.uba.ar", "t", "c", 100, 100, 10, 6, "published")
    config.addEvent("tarrachea@fi.uba.ar", "t", "c", 100, 100, 10, 5, "published")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 3}
    otherQuery = {"event_id": 2, "tickets": 2}
    client.post("/user/event/reservation", json=query, headers=headers)
    client.post("/user/event/reservation", json=otherQuery, headers=headers)
    response = client.get("/user/reservations", headers=headers)
    config.clear()
    assert len(response.json()) == 2

def test27_viewOnlyPublishedEvents():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "sport", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "cinema", 100, 100, 10, 10, "draft")
    config.addEvent("gmovia@fi.uba.ar", "soccer", "cinema", 100, 100, 10, 10, "draft")
    config.addEvent("gmovia@fi.uba.ar", "movies", "cinema", 100, 100, 10, 10, "published")
    query = {"title": "soccer"}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert len(response.json()) == 1

def test28_viewOnlyPublishedEvents():
    headers = config.addUser("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 150, 125, 10, 10, "published")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 75, 80, 10, 10, "draft")
    query = {"latitude": 75, "longitude": 90}
    response = client.get("/user/events", params=query, headers=headers)
    config.clear()
    assert response.json()[0]["Event"]["longitude"] == 100
    assert response.json()[1]["Event"]["longitude"] == 125

def test29_ifTheEventIsntPublishedThenWhenTheUserReserveItTheStatusCodeWillBe403():
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "draft")
    headers = config.addUser("rlareu@fi.uba.ar")
    query = {"event_id": 1, "tickets": 2}
    response = client.post("/user/event/reservation", json=query, headers=headers)
    config.clear()
    assert response.status_code == 403