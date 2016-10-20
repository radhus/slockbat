import datetime
import json
import sys

import mongoengine
from slacksocket import SlackSocket

from models.message import Message


class Bot:
    def __init__(self, config):
        self.s = SlackSocket(config['slack'].get('token'))

        # Wrap this in the connect call?
        self.mongo_db = config['main'].get('mongo_db')
        self.mongo_host = config['main'].get('mongo_host')
        self.mongo_port = config['main'].getint('mongo_port')

        # Is this a good way to handle mongo connection? Seems weird.
        self.mongo = mongoengine
        self.mongo.connect(self.mongo_db,
                           host=self.mongo_host,
                           port=self.mongo_port)

    def start(self):
        for event in self.s.events():
            if event.type == 'message':
                # TODO Pass when message has subtype, eg. message_changed.
                # Maybe do this in a nicer way.
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
