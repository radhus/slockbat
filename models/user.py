import datetime
from mongoengine import Document, StringField, DateTimeField


class User(Document):
    id = StringField(required=True)
    name = StringField(required=True)
    real_name = StringField()
    timestamp = DateTimeField(default=datetime.datetime.utcnow())