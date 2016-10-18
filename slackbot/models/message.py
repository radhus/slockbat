from mongoengine import Document,StringField,DateTimeField


class Message(Document):
    user = StringField(required=True)
    text = StringField(required=True)
    timestamp = DateTimeField(required=True)
