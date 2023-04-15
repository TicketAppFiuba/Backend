from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheQuestionIsAddedSuccessfullyThenStatusCodeIs200():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)  
    question = {"event_id": 1, "question": "a", "response": "b"}
    response = client.post("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheQuestionIsNotAddedNSuccessfullyBecauseEventNotExistThenTheStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)  
    question = {"event_id": 3, "question": "a", "response": "b"}
    response = client.post("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test03_ifTheQuestionIsDeletedSuccessfullyThenStatusCodeIs200():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)  
    question = {"event_id": 1, "question": "a", "response": "b"}
    client.post("/organizer/event/faq", json=question, headers=headers)
    question = {"id": 1, "event_id": 1}
    response = client.delete("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 200

def test04_ifTheQuestionIsNotDeletedSuccessfullyBecauseEventNotExistThenStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)  
    question = {"id": 1, "event_id": 2}
    response = client.delete("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test05_ifTheQuestionIsNotDeletedSuccessfullyBecauseQuestionNotExistThenStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)  
    question = {"id": 2, "event_id": 1}
    response = client.delete("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test06_ifTheQuestionIsNotDeletedSuccessfullyBecauseRLareuDoesntHavePermission():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)  
    question = {"event_id": 1, "question": "a", "response": "b"}
    client.post("/organizer/event/faq", json=question, headers=headers)
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    question = {"id": 1, "event_id": 1}
    response = client.delete("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test07_ifTheQuestionIsUpdatedSuccessfullyThenStatusCodeIs200():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)  
    question = {"event_id": 1, "question": "a", "response": "b"}
    client.post("/organizer/event/faq", json=question, headers=headers)
    question = {"id": 1, "event_id": 1, "question": "c", "response": "d"}
    response = client.put("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 200

def test08_ifTheQuestionIsNotUpdatedSuccessfullyBecauseEventNotExistThenStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)  
    question = {"id": 1, "event_id": 5, "question": "c", "response": "d"}
    response = client.put("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test09_ifTheQuestionIsNotUpdatedSuccessfullyBecauseQuestionNotExistThenStatusCodeIs404():
    headers = config.addOrganizer("gmovia@fi.uba.ar")
    config.addEvent("gmovia@fi.uba.ar", "t", "c", 100, 100, 10, 10)  
    question = {"id": 4, "event_id": 1, "question": "c", "response": "d"}
    response = client.put("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test10_ifTheQuestionIsNotUpdatedSuccessfullyBecauseRLareuDoesntHavePermission():
    headers = config.addOrganizer("ldefeo@fi.uba.ar")
    config.addEvent("ldefeo@fi.uba.ar", "t", "c", 100, 100, 10, 10)      
    question = {"event_id": 1, "question": "a", "response": "b"}
    client.post("/organizer/event/faq", json=question, headers=headers)
    headers = config.addOrganizer("rlareu@fi.uba.ar")
    question = {"id": 1, "event_id": 1, "question": "c", "response": "d"}
    response = client.put("/organizer/event/faq", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404