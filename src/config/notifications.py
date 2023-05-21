from sqlalchemy.orm import Session
from src.models.event import Event
from src.models.user import User
from firebase_admin import messaging
from src.schemas.notification import NotificationSchema
import datetime
from main import lock, pendingEvents

REMINDER_TIME_HOURS = 24

def send_notification(event_id: int, notification: NotificationSchema):
    message = messaging.Message(
        notification=messaging.Notification(
            title=notification.title,
            body=notification.description,
        ),
        topic=str(event_id)
    )
    messaging.send(message)

def create_subscription(user_id: int, event_id: int, db: Session):
    token = db.query(User).filter(User.id == user_id).first().firebase_token
    if token:
        response = messaging.subscribe_to_topic(token, str(event_id))
        return response

def create_scheduled_notification(event_db: Event):
    schedule_time = event_db.date - datetime.timedelta(hours=REMINDER_TIME_HOURS)
    with lock:
        pendingEvents[event_db.id] = schedule_time
    print('Successfully scheduled notification at', schedule_time, ': ')

def delete_event_notifications(event_db: Event):
    with lock:
        pendingEvents.pop(event_db.id)
