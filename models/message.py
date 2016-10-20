import datetime
from mongoengine import Document, StringField, DateTimeField


class Message(Document):
    user = StringField(required=True)
    channel = StringField(required=True)
    text = StringField(required=True)
    timestamp = DateTimeField(default=datetime.datetime.utcnow(), required=True)
