from src.schemas.event import EventSchema
from src.models.event import Event
from src.models.section import Section
from src.models.faq import FAQ
from src.models.event_authorizer import EventAuthorizer

def addRelationsToEvent(event_db: Event, event: EventSchema):
    for section in event.agenda:
        event_db.sections.append(Section(**section.dict()))
    
    for faq in event.faqs:
        event_db.faqs.append(FAQ(**faq.dict()))

    for authorizer in event.authorizers:
        event_db.authorizers.append(EventAuthorizer(**authorizer.dict()))


def updateRelationsToEvent(event_db: Event, event):
    for section in event.pop('agenda', []):
        event_db.sections.append(Section(**section))

    for faq in event.pop('faqs', []):
        event_db.faqs.append(FAQ(**faq))