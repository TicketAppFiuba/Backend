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
            query = f"INSERT INTO users (email, name, login) VALUES ('{email}', '{email}', 'True')"
            c.execute(query)
            token = jwt.create(email)["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            return headers
    
    def addOrganizer(self, email: str):
        with engine.connect() as c:
            query = f"INSERT INTO organizers (email, name, login) VALUES ('{email}', '{email}', 'True')"
            c.execute(query)
            token = jwt.create(email)["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            return headers
        
    def addAuthorizer(self, email: str):
        with engine.connect() as c:
            query = f"INSERT INTO authorizers (email, name, login) VALUES ('{email}', '{email}', 'True')"
            c.execute(query)
            token = jwt.create(email)["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            return headers
        
    def addAdmin(self):
        token = jwt.create("admin")["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        return headers
        
    def addPermissionScan(self, email: str, event_id: int):
        with engine.connect() as c:
            query = f"INSERT INTO eventsauthorizers (email, event_id) VALUES ('{email}', {event_id})"
            c.execute(query)

    def addEvent(self, email, title, category, latitude, longitude, capacity, vacancies, state):
        with engine.connect() as c:
            query = f"INSERT INTO events (organizer_email, description, capacity, init_date, end_date, title, category, direction, latitude, longitude, vacancies, pic_id, state, create_date) VALUES ('{email}', 'a', '{capacity}', '{datetime.datetime.now()}', '{datetime.datetime.now()}', '{title}', '{category}', 'str', '{latitude}', '{longitude}', '{vacancies}', 0, '{state}', '{datetime.datetime.now()}') RETURNING events.id"
            return c.execute(query).fetchone()[0]

    def clear(self):
        with engine.connect() as c:
            c.execute(text("DELETE FROM attendances"))
            c.execute(text("DELETE FROM eventsauthorizers"))
            c.execute(text("DELETE FROM calendar"))
            
            c.execute(text("DELETE FROM faqs"))
            c.execute(text("DELETE FROM sections"))
            c.execute(text("DELETE FROM images"))

            c.execute(text("DELETE FROM reservations"))
            c.execute(text("DELETE FROM suspensions"))
            c.execute(text("DELETE FROM favorites"))
            c.execute(text("DELETE FROM complaints"))
            c.execute(text("DELETE FROM users"))
            c.execute(text("DELETE FROM authorizers"))
            c.execute(text("DELETE FROM events"))
            c.execute(text("DELETE FROM organizers"))