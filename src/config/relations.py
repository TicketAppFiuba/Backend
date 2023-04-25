from src.schemas.event import EventSchema
from src.models.event import Event
from src.models.section import Section
from src.models.faq import FAQ
from src.models.image import Image
from src.models.event_authorizer import EventAuthorizer

def addRelationsToEvent(event_db: Event, event: EventSchema, email: str):
    for section in event.agenda:
        event_db.sections.append(Section(**section.dict()))
    
    for faq in event.faqs:
        event_db.faqs.append(FAQ(**faq.dict()))

    for image in event.images:
        event_db.images.append(Image(**image.dict()))

    for authorizer in event.authorizers:
        event_db.authorizers.append(EventAuthorizer(**authorizer.dict()))
    
    event_db.authorizers.append(EventAuthorizer(event_id=event_db.id, email=email))


def updateRelationsToEvent(event_db: Event, event):
    event_db.sections = []
    for section in event.pop('agenda', []):
        event_db.sections.append(Section(**section))

    event_db.faqs = []
    for faq in event.pop('faqs', []):
        event_db.faqs.append(FAQ(**faq))

    event_db.images = []
    for image in event.pop('images', []):
        event_db.images.append(Image(**image))