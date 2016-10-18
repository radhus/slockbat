#!/usr/bin/env python3
from slackbot.bot import Bot


def run():
    slackbot = Bot()

    try:
        slackbot.start()
    except KeyboardInterrupt:
        slackbot.quit()


if __name__ == '__main__':
    run()