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
            c.execute(text("INSERT INTO organizers (email, name, login) VALUES ('rlareu@fi.uba.ar', 'rlareu', 'True')"))

    def setUpImages(self):
        with engine.connect() as c:
            c.execute(text("INSERT INTO organizers (email, name, login) VALUES ('rlareu@fi.uba.ar', 'rlareu', 'True')"))
            c.execute(text("INSERT INTO events (organizer_email, description, capacity, date, title, category, direction, latitude, length, vacancies) VALUES ('rlareu@fi.uba.ar', 'a', 100, '2023-04-01', 'str', 'str', 'str', 100, 100, 100)"))
            c.execute(text("INSERT INTO events (organizer_email, description, capacity, date, title, category, direction, latitude, length, vacancies) VALUES ('rlareu@fi.uba.ar', 'a', 100, '2023-04-01', 'str', 'str', 'str', 100, 100, 100)"))

    def setUpFAQ(self):
         with engine.connect() as c:
            c.execute(text("INSERT INTO organizers (email, name, login) VALUES ('ldefeo@fi.uba.ar', 'ldefeo', 'True')"))
            c.execute(text("INSERT INTO events (organizer_email, description, capacity, date, title, category, direction, latitude, length, vacancies) VALUES ('ldefeo@fi.uba.ar', 'a', 100, '2023-04-01', 'str', 'str', 'str', 100, 100, 100)"))

    def clear(self):
        with engine.connect() as c:
            c.execute(text("DELETE FROM organizers"))
            c.execute(text("DELETE FROM users"))
            c.execute(text("DELETE FROM events"))
            c.execute(text("DELETE FROM images"))

