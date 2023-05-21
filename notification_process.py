import datetime
import time
from src.models.event import Event
from src.config.db import SessionLocal
from src.config.notifications import send_notification
from src.schemas.notification import NotificationSchema
from sqlalchemy.orm import Session

def reminder_notifications():
    db = SessionLocal()
    while True:
        events = db.query(Event).filter(Event.state == "published")
        for event_db in events:
            notification_time = event_db.date - datetime.timedelta(hours=24)
            if notification_time <= datetime.datetime.now:
                notify(event_db)
                event_db.notified = True
        time.sleep(3600) # cada 1 hs

def notify(event_db):
    event_name = event_db.name
    notification = NotificationSchema(
        title=f'Falta un día para \"{event_name}\"!',
        description=f'Recuerda que el evento \"{event_name}\" comienza en 24 hs'
    )
    send_notification(event_db.id, notification)