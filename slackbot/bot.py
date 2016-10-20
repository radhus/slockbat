import datetime
import json
import sys

import mongoengine
from slacksocket import SlackSocket

from models.message import Message


class Bot:
    def __init__(self, config):
        self.s = SlackSocket(config['slack'].get('token'))

        # Is this a good way to handle mongo connection? Seems weird.
        # TODO check for connection timeout
        self.mongo = mongoengine
        self.mongo.connect(config['mongo'].get('db'),
                           host=config['mongo'].get('host'),
                           port=config['mongo'].getint('port'))

    def start(self):
        for event in self.s.events():
            if event.type == 'message':
                # TODO Pass when message has subtype, eg. message_changed.
                # Maybe do this in a nicer way. Use event.event (dict)?
                if 'subtype' in event.json:
                    pass
                else:
                    event_json = json.loads(event.json)
                    message = Message(user=event_json['user'],
                                      channel=event_json['channel'],
                                      text=event_json['text'].strip(),
                                      timestamp=datetime.datetime.utcnow())
                    message.save()

    def quit(self):
        self.s.close()
        self.mongo.connection.disconnect()
        sys.exit(0)
