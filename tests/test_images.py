from fastapi.testclient import TestClient
from main import app
from src.objects.jwt import JWTToken
from tests.setUp import TestSetUp

config = TestSetUp()
client = TestClient(app)
jwt = JWTToken("HS256", 15)

def test01_addImageOK():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 1, "link": "a"}
    response = client.post("/event/images/add", json=image, headers=headers)
    config.clearImages()
    assert response.status_code == 200

def test02_addImageNOKBecauseEventNotExist():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 3, "link": "a"}
    response = client.post("/event/images/add", json=image, headers=headers)
    config.clearImages()
    assert response.status_code == 404

def test03_updateImageOK():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 1, "link": "a"}
    client.post("/event/images/add", json=image, headers=headers)
    new_image = {"event_id": 1, "id": 1, "link": "b"}
    response = client.put("/event/images/update", json=new_image, headers=headers)
    config.clearImages()
    assert response.status_code == 200

def test04_updateImageNOKBecauseImgNotExist():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 1, "link": "a"}
    client.post("/event/images/add", json=image, headers=headers)
    new_image = {"event_id": 1, "id": 2, "link": "b"}
    response = client.put("/event/images/update", json=new_image, headers=headers)
    config.clearImages()
    assert response.status_code == 404

def test05_updateImageNOKBecauseEventNotExist():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 1, "link": "a"}
    client.post("/event/images/add", json=image, headers=headers)
    new_image = {"event_id": 3, "id": 1, "link": "b"}
    response = client.put("/event/images/update", json=new_image, headers=headers)
    config.clearImages()
    assert response.status_code == 404

def test06_deleteImageOK():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 1, "link": "a"}
    client.post("/event/images/add", json=image, headers=headers)
    del_image = {"id": 1, "event_id": 1}
    response = client.delete("/event/images/delete", json=del_image, headers=headers)
    config.clearImages()
    assert response.status_code == 200

def test07_deleteImageNOKBecauseImgNotExist():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 1, "link": "a"}
    client.post("/event/images/add", json=image, headers=headers)
    del_image = {"id": 3, "event_id": 1}
    response = client.delete("/event/images/delete", json=del_image, headers=headers)
    config.clearImages()
    assert response.status_code == 404

def test08_deleteImageNOKBecauseEventNotExist():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 1, "link": "a"}
    client.post("/event/images/add", json=image, headers=headers)
    del_image = {"id": 1, "event_id": 3}
    response = client.delete("/event/images/delete", json=del_image, headers=headers)
    config.clearImages()
    assert response.status_code == 404

def test09_updateImageNOKBecauseImgDoestNotBelongToTheEvent():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 1, "link": "a"}
    client.post("/event/images/add", json=image, headers=headers)
    new_image = {"event_id": 2, "id": 1, "link": "b"}
    response = client.put("/event/images/update", json=new_image, headers=headers)
    config.clearImages()
    assert response.status_code == 404

def test10_deleteImageNOKBecauseImgDoestNotBelongToTheEvent():
    config.setUpImages()
    token = jwt.create("rlareu@fi.uba.ar")["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    image = {"event_id": 1, "link": "a"}
    client.post("/event/images/add", json=image, headers=headers)
    new_image = {"id": 1, "event_id": 2}
    response = client.delete("/event/images/delete", json=new_image, headers=headers)
    config.clearImages()
    assert response.status_code == 404