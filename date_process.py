import datetime
from src.models.event import Event
from src.config.db import SessionLocal
from src.config.event import *

def change_status_to_finalished():
    db = SessionLocal()
    events = db.query(Event).filter(Event.state == "published").all()
    for event_db in events:
        if datetime.datetime.now() > event_db.date:
            finish(event_db, db)
    db.close()

