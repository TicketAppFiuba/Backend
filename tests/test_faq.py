from fastapi.testclient import TestClient
from main import app
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)

def test01_ifTheQuestionIsAddedSuccessfullyThenStatusCodeIs200():
    headers = config.setUpEvent("ldefeo@fi.uba.ar")
    question = {"event_id": 1, "question": "a", "response": "b"}
    response = client.post("/event/question/add", json=question, headers=headers)
    config.clear()
    assert response.status_code == 200

def test02_ifTheQuestionIsNotAddedNSuccessfullyBecauseEventNotExistThenTheStatusCodeIs404():
    headers = config.setUpEvent("ldefeo@fi.uba.ar")
    question = {"event_id": 3, "question": "a", "response": "b"}
    response = client.post("/event/question/add", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test03_ifTheQuestionIsDeletedSuccessfullyThenStatusCodeIs200():
    headers = config.setUpEvent("ldefeo@fi.uba.ar")
    question = {"event_id": 1, "question": "a", "response": "b"}
    client.post("/event/question/add", json=question, headers=headers)
    question = {"question_id": 1, "event_id": 1}
    response = client.delete("/event/question/delete", json=question, headers=headers)
    config.clear()
    assert response.status_code == 200

def test04_ifTheQuestionIsNotDeletedSuccessfullyBecauseEventNotExistThenStatusCodeIs404():
    headers = config.setUpEvent("ldefeo@fi.uba.ar")
    question = {"question_id": 1, "event_id": 2}
    response = client.delete("/event/question/delete", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test05_ifTheQuestionIsNotDeletedSuccessfullyBecauseQuestionNotExistThenStatusCodeIs404():
    headers = config.setUpEvent("ldefeo@fi.uba.ar")
    question = {"question_id": 2, "event_id": 1}
    response = client.delete("/event/question/delete", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404

def test06_ifTheQuestionIsNotDeletedSuccessfullyBecauseRLareuDoesntHavePermission():
    headers = config.setUpEvent("ldefeo@fi.uba.ar")
    question = {"event_id": 1, "question": "a", "response": "b"}
    client.post("/event/question/add", json=question, headers=headers)
    headers = config.setUpEvent("rlareu@fi.uba.ar")
    question = {"question_id": 1, "event_id": 1}
    response = client.delete("/event/question/delete", json=question, headers=headers)
    config.clear()
    assert response.status_code == 404