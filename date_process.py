from src.models.event import Event
from src.config.db import SessionLocal
from src.config.event import *
import datetime
import time

def change_status_to_finalished(stop_flag):
    db = SessionLocal()
    while not stop_flag.is_set():
        events = db.query(Event).filter(Event.state == "published").all()
        for event_db in events:
            if datetime.datetime.now() > event_db.end_date:
                finish(event_db, db)
                time.sleep(60)
    db.close()

