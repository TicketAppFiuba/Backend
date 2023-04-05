from fastapi.testclient import TestClient
from main import app
from src.objects.jwt import JWTToken
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)
jwt = JWTToken("HS256", 15)

def test01_ifAddQuestionOKThenStatusCodeIs200():
    config.setUpFAQ()
    token = jwt.create("ldefeo@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    question = {"event_id": 1, "question": "a", "response": "b"}
    response = client.post("/event/question/add", json=question, headers=headers)
    assert response.status_code == 200
    config.clear()
    assert 200 == 200
