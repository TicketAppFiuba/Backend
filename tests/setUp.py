from src.config.db import engine
from sqlalchemy import text
from fastapi.testclient import TestClient
from src.objects.jwt import JWTToken
from main import app

client = TestClient(app)
jwt = JWTToken("HS256", 15)

class TestSetUp:
    def addUser(self, email: str):
        with engine.connect() as c:
            query = "INSERT INTO users (email, name, login) VALUES (:email, 'ldefeo', 'True')"
            c.execute(query, {'email': email})
            token = jwt.create(email)["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            return headers
    
    def addOrganizer(self, email: str):
        with engine.connect() as c:
            query = "INSERT INTO organizers (email, name, login) VALUES (:email, 'ldefeo', 'True')"
            c.execute(query, {'email': email})
            token = jwt.create(email)["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            return headers

    def addEvent(self, email, title, category, latitude, longitude):
           with engine.connect() as c:
            query = "INSERT INTO events (organizer_email, description, capacity, date, title, category, direction, latitude, longitude, vacancies) VALUES (:email, 'a', 100, '2023-04-01', :title, :category, 'str', :latitude, :longitude, 100)"
            c.execute(query, {'email': email, 'title': title, 'category': category, 'latitude':latitude, "longitude": longitude})

    def clear(self):
        with engine.connect() as c:
            c.execute(text("DELETE FROM organizers"))
            c.execute(text("DELETE FROM users"))
            c.execute(text("DELETE FROM events"))
            c.execute(text("DELETE FROM images"))
            c.execute(text("DELETE FROM faqs"))
            c.execute(text("DELETE FROM reservations"))