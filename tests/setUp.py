from src.config.db import engine
from sqlalchemy import text
from fastapi.testclient import TestClient
from src.objects.jwt import JWTToken
from main import app
import datetime

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
        
    def addAuthorizer(self, email: str):
        with engine.connect() as c:
            query = "INSERT INTO authorizers (email, name, login) VALUES (:email, 'ldefeo', 'True')"
            c.execute(query, {'email': email})
            token = jwt.create(email)["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            return headers
        
    def addAdmin(self):
        token = jwt.create("admin")["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        return headers
        
    def addPermissionScan(self, email: str, event_id: int):
        with engine.connect() as c:
            query = "INSERT INTO eventsauthorizers (email, event_id) VALUES (:email, :event_id)"
            c.execute(query, {'email': email, 'event_id': event_id})

    def addEvent(self, email, title, category, latitude, longitude, capacity, vacancies, state):
        with engine.connect() as c:
            query = "INSERT INTO events (organizer_email, description, capacity, date, title, category, direction, latitude, longitude, vacancies, pic_id, state) VALUES (:email, 'a', :capacity, :date, :title, :category, 'str', :latitude, :longitude, :vacancies, 0, :state)"
            c.execute(query, {'email': email, "capacity": capacity, 'title': title, 'category': category, 'latitude':latitude, "longitude": longitude, "vacancies": vacancies, 'state': state, 'date': datetime.datetime.now()})

    def clear(self):
        with engine.connect() as c:
            c.execute(text("DELETE FROM organizers"))
            c.execute(text("DELETE FROM users"))
            c.execute(text("DELETE FROM events"))
            c.execute(text("DELETE FROM images"))
            c.execute(text("DELETE FROM faqs"))
            c.execute(text("DELETE FROM reservations"))
            c.execute(text("DELETE FROM sections"))
            c.execute(text("DELETE FROM authorizers"))
            c.execute(text("DELETE FROM eventsauthorizers"))
            c.execute(text("DELETE FROM complaints"))