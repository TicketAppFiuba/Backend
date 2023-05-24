from sqlalchemy.orm import Session
from src.models.event import Event
from src.models.user import User
from firebase_admin import messaging
from src.schemas.notification import NotificationSchema

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
        response = messaging.subscribe_to_topic([token], str(event_id))
        return response
