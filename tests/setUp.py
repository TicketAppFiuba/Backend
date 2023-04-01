from src.config.db import engine
from sqlalchemy import text
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestSetUp:
    def setUp(self):
        with engine.connect() as c:
            c.execute(text("INSERT INTO users (email, name, login) VALUES ('ldefeo@fi.uba.ar', 'ldefeo', 'True')"))
            c.execute(text("INSERT INTO organizers (email, name, login) VALUES ('cbravor@fi.uba.ar', 'cbravor', 'True')"))
            c.execute(text("INSERT INTO organizers (email, name, login) VALUES ('rlareu@fi.uba.ar', 'cbravor', 'True')"))

    def clear(self):
        with engine.connect() as c:
            c.execute(text("DELETE FROM organizers WHERE email='rlareu@fi.uba.ar'"))
            c.execute(text("DELETE FROM users WHERE email='ldefeo@fi.uba.ar'"))
            c.execute(text("DELETE FROM organizers WHERE email='cbravor@fi.uba.ar'"))
            c.execute(text("DELETE FROM events"))

    def setUpImages(self):
        with engine.connect() as c:
            c.execute(text("INSERT INTO organizers (email, name, login) VALUES ('rlareu@fi.uba.ar', 'cbravor', 'True')"))
            c.execute(text("INSERT INTO events (organizer_email, description, tickets, date, title, category, direction, latitude, length) VALUES ('rlareu@fi.uba.ar', 'a', 100, '2023-04-01', 'str', 'str', 'str', 'str', 'str')"))
            c.execute(text("INSERT INTO events (organizer_email, description, tickets, date, title, category, direction, latitude, length) VALUES ('rlareu@fi.uba.ar', 'a', 100, '2023-04-01', 'str', 'str', 'str', 'str', 'str')"))

    def clearImages(self):
        with engine.connect() as c:
            c.execute(text("DELETE FROM organizers WHERE email='rlareu@fi.uba.ar'"))
            c.execute(text("DELETE FROM events"))
            c.execute(text("DELETE FROM images"))