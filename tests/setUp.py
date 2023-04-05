from src.config.db import engine
from sqlalchemy import text
from fastapi.testclient import TestClient
from src.objects.jwt import JWTToken
from main import app

client = TestClient(app)
jwt = JWTToken("HS256", 15)

class TestSetUp:
    def setUpAccess(self, email: str, type: str):
         with engine.connect() as c:
            if type == "user":
                query = "INSERT INTO users (email, name, login) VALUES (:email, 'ldefeo', 'True')"
            if type == "organizer":
                query = "INSERT INTO organizers (email, name, login) VALUES (:email, 'ldefeo', 'True')"
            c.execute(query, {'email': email})
            token = jwt.create(email)["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            return headers

    def setUpEvent(self, email: str):
         with engine.connect() as c:
            query = "INSERT INTO organizers (email, name, login) VALUES (:email, 'ldefeo', 'True')"
            c.execute(query, {'email': email})
            otherQuery = "INSERT INTO events (organizer_email, description, capacity, date, title, category, direction, latitude, length, vacancies) VALUES (:email, 'a', 100, '2023-04-01', 'str', 'str', 'str', 100, 100, 100)"
            c.execute(otherQuery, {"email": email})
            token = jwt.create(email)["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            return headers

    def clear(self):
        with engine.connect() as c:
            c.execute(text("DELETE FROM organizers"))
            c.execute(text("DELETE FROM users"))
            c.execute(text("DELETE FROM events"))
            c.execute(text("DELETE FROM images"))

