from fastapi.testclient import TestClient
from main import app
from src.objects.jwt import JWTToken
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)
jwt = JWTToken("HS256", 15)

def test01_ifAddImageOKThenStatusCodeIs200():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    assert response.status_code == 200
    config.clear()

def test02_ifAddImageNOKBecauseEventNotExistThenTheStatusCodeIs404():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/event/images/add", json={"event_id": 3, "link": "a"}, headers=headers)
    assert response.status_code == 404
    config.clear()

def test03_ifUpdateImageOKThenTheStatusCodeIs200():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.put("/event/images/update", json={"event_id": 1, "id": 1, "link": "b"}, headers=headers)
    assert response.status_code == 200
    config.clear()

def test04_ifUpdateImageNOKBecauseImgNotExistThenTheStatusCodeIs404():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.put("/event/images/update", json={"event_id": 1, "id": 2, "link": "b"}, headers=headers)
    assert response.status_code == 404
    config.clear()

def test05_ifUpdateImageNOKBecauseEventNotExistThenTheStatusCodeIs404():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.put("/event/images/update", json={"event_id": 3, "id": 1, "link": "b"}, headers=headers)
    assert response.status_code == 404
    config.clear()

def test06_ifDeleteImageOKThenTheStatusCodeIs200():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.delete("/event/images/delete", json={"id": 1, "event_id": 1}, headers=headers)
    assert response.status_code == 200
    config.clear()

def test07_ifDeleteImageNOKBecauseImgNotExistThenTheStatusCodeIs404():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.delete("/event/images/delete", json={"id": 3, "event_id": 1}, headers=headers)
    assert response.status_code == 404
    config.clear()

def test08_ifDeleteImageNOKBecauseEventNotExistThenTheStatusCodeIs404():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.delete("/event/images/delete", json={"id": 1, "event_id": 3}, headers=headers)
    assert response.status_code == 404
    config.clear()

def test09_ifUpdateImageNOKBecauseImgDoestNotBelongToTheEventThenStatusCodeIs404():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.put("/event/images/update", json={"event_id": 2, "id": 1, "link": "b"}, headers=headers)
    assert response.status_code == 404
    config.clear()

def test10_ifDeleteImageNOKBecauseImgDoestNotBelongToTheEventThenTheStatusCodeIs404():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.delete("/event/images/delete", json={"id": 1, "event_id": 2}, headers=headers)
    assert response.status_code == 404
    config.clear()

def test11_addImageOK():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    response = client.get("/event/images", params={"id": 1, "event_id": 1}, headers=headers)
    assert response.json()[0]["link"] == "a"
    config.clear()

def test12_updateImageOK():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json= {"event_id": 1, "link": "a"}, headers=headers)
    client.put("/event/images/update", json={"event_id": 1, "id": 1, "link": "b"}, headers=headers)
    response = client.get("/event/images", params={"id": 1, "event_id": 1}, headers=headers)
    assert response.json()[0]["link"] == "b"
    config.clear()

def test13_deleteImageOK():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/event/images/add", json={"event_id": 1, "link": "a"}, headers=headers)
    client.delete("/event/images/delete", json={"event_id": 1, "id": 1}, headers=headers)
    response = client.get("/event/images", params={"event_id": 1, "id": 1}, headers=headers)
    assert response.json() == []
    config.clear()