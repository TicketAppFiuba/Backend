from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheQuestionIsAddedSuccessfullyThenStatusCodeIs200():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    question = {"event_id": event_id, "question": "a", "response": "b"}
    response = client.post("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheQuestionIsNotAddedNSuccessfullyBecauseEventNotExistThenTheStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    question = {"event_id": 3, "question": "a", "response": "b"}
    response = client.post("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test03_ifTheQuestionIsDeletedSuccessfullyThenStatusCodeIs200():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    question = {"event_id": event_id, "question": "a", "response": "b"}
    faq = client.post("/organizer/event/faq", json=question, headers=headers)
    question = {"id": faq.json()["id"], "event_id": event_id}
    response = client.delete("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 200

def test04_ifTheQuestionIsNotDeletedSuccessfullyBecauseTheQuestionNotExistThenStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    question = {"id": 100}
    response = client.delete("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test05_ifTheQuestionIsNotDeletedSuccessfullyBecauseQuestionNotExistThenStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    question = {"id": 2}
    response = client.delete("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test06_ifTheQuestionIsNotDeletedSuccessfullyBecauseRLareuDoesntHavePermission():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    question = {"event_id": event_id, "question": "a", "response": "b"}
    client.post("/organizer/event/faq", json=question, headers=headers)
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    question = {"id": 1}
    response = client.delete("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test07_ifTheQuestionIsUpdatedSuccessfullyThenStatusCodeIs200():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    event_id = config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    question = {"event_id": event_id, "question": "a", "response": "b"}
    faq = client.post("/organizer/event/faq", json=question, headers=headers)
    question = {"id": faq.json()["id"], "question": "c", "response": "d"}
    response = client.put("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 200

def test08_ifTheQuestionIsNotUpdatedSuccessfullyBecauseQuestionNotExistThenStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    question = {"id": 100, "question": "c", "response": "d"}
    response = client.put("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test09_ifTheQuestionIsNotUpdatedSuccessfullyBecauseQuestionNotExistThenStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")  
    question = {"id": 4, "question": "c", "response": "d"}
    response = client.put("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test10_ifTheQuestionIsNotUpdatedSuccessfullyBecauseRLareuDoesntHavePermission():
    headers = config.addOrganizer("ldefeo@fi.uba.ar")
    event_id = config.addEvent("ldefeo@fi.uba.ar", "t", "c", 100, 100, 10, 10, "published")      
    question = {"event_id": event_id, "question": "a", "response": "b"}
    client.post("/organizer/event/faq", json=question, headers=headers)
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    question = {"id": 1, "question": "c", "response": "d"}
    response = client.put("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404