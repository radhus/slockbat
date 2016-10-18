import sys
import json
import datetime
import mongoengine

from slacksocket import SlackSocket
from slackbot.models.message import Message

"""
Put this in a config file, together with other things such as mongo URI.
xoxb-84282495654-KHPGRmPs7x1cyB534EuhCZi8
"""


class Bot:
    def __init__(self):
        self.s = SlackSocket('xoxb-84282495654-KHPGRmPs7x1cyB534EuhCZi8')

        # Is this a good way to handle mongo connection? Seems weird.
        self.mongo = mongoengine
        self.mongo.connect('slackbot', host='10.0.1.5', port=27017)

    def start(self):
        for event in self.s.events():
            if event.type == 'message':
                event_json = json.loads(event.json)
                print(event_json)
                message = Message(user=event_json['user'], text=event_json['text'], timestamp=datetime.datetime.now())
                print(message.user)

    def quit(self):
        self.s.close()
        self.mongo.connection.disconnect()
        sys.exit(0)