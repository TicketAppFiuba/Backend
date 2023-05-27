from sqlalchemy.orm import Session
from src.models.event import Event
from src.models.user import User
from firebase_admin import messaging
from src.schemas.notification import NotificationSchema
from fastapi import HTTPException
from src.config import image, event

def send_notification(event_id: int, notification: NotificationSchema, db: Session):
    event_db = event.get(event_id, db)
    message = messaging.Message(
        notification=messaging.Notification(
            title=notification.title,
            body=notification.description,
            image=image.getCoverImage(event_db.pic_id, db).link
        ),
        data={ 'event_id': str(event_id) },
        topic=str(event_id)
    )
    send = messaging.send(message)
    print("SEND NOTIF con id: " +send)
    return send

def create_subscription(user_id: int, event_id: int, db: Session):
    token = db.query(User).filter(User.id == user_id).first().firebase_token
    if token:
        response = messaging.subscribe_to_topic([token], str(event_id))
        if response.success_count == 0:
            raise HTTPException(status_code=400, detail= (f"Failed to subscribe to topic {str(event_id)} due to {list(map(lambda e: e.reason,response.errors))}"))
        print("SE CREARON " +str(response.success_count) + " SUBSCRIPCIONES")
        return response
    else:
        print('No hay token FCM seteado para el usuario')
