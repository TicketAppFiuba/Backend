import datetime
import time
from src.models.event import Event
from src.config.db import SessionLocal
from src.config.notifications import send_notification
from src.schemas.notification import NotificationSchema
from firebase_admin import get_app

def reminder_notifications(stop_flag):
    db = SessionLocal()
    while not stop_flag.is_set(): # muere 1hs despues, cuando termina el sleep
        events = db.query(Event).filter(Event.state == "published")
        for event_db in events:
            if should_notify_event(event_db):
                print("Proceso de notificaciones - enviado a evento: " + event_db.title)
                notify(event_db)
                event_db.notified = True
        time.sleep(3600) # cada 1 hs
    db.close()

def should_notify_event(event_db):
    prev_day = datetime.datetime.now() - datetime.timedelta(hours=24)
    return event_db.date >= prev_day and event_db.date < datetime.datetime.now() and event_db.notified == False

def notify(event_db):
    event_name = event_db.title
    notification = NotificationSchema(
        title=f'Falta un día para \"{event_name}\"!',
        description=f'Recuerda que el evento \"{event_name}\" comienza en 24 hs'
    )
    send_notification(event_db.id, notification)