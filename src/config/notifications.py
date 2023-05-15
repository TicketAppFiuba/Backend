from sqlalchemy.orm import Session
from src.models.event import Event
from src.models.user import User
from firebase_admin import messaging
from src.schemas.notification import NotificationSchema
import datetime

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
    event_hour = event_db.date.strftime('%H:%M')
    schedule_time = event_db.date - datetime.timedelta(hours=24)

    # message = messaging.Message(
    #     notification=messaging.Notification(
    #         title=f'Falta poco para \'{event_db.title}\'!',
    #         body=f'Recuerda: faltan 24hs para el inicio de \'{event_db.title}\', que comienza a las {event_hour} hs.'
    #     ),
    #     topic=str(event_db.id),
    #     schedule_time=schedule_time # revisar, si no funciona tengo que hacer un proceso que chequee los times
    # )
    # response = messaging.send(message)
    print('Successfully scheduled notification at', schedule_time, ': ')

def delete_event_notifications(event_db: Event):
    # depende de como se seteen las scheduled notifications. 
    print('Successfully deleted all scheduled messages for event:', event_db.id)
