import datetime
from src.config.event import get
from src.config.db import get_db
from src.config.notifications import send_notification
from src.schemas.notification import NotificationSchema

def reminder_notifications(pendingEvents, lock):
    db = get_db()
    while True:
        with lock:
            for event_id, time in pendingEvents.items():
                if time <= datetime.datetime.now:
                    notify(event_id)
                    pendingEvents.remove(event_id, db)
        time.sleep(3600) # cada 1 hs

def notify(event_id):
    event_name = get(event_id).name
    notification = NotificationSchema(
        title=f'Falta un día para \"{event_name}\"!',
        description=f'Recuerda que el evento \"{event_name}\" comienza en 24 hs'
    )
    send_notification(event_id, notification)