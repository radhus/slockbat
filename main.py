#!/usr/bin/env python3
import sys

from slackbot.bot import Bot


def run():
    from utils import parse_config
    config = parse_config('config.ini')

    if 'main' not in config:
        print("Missing main in config.")
        sys.exit(0)

    if 'slack' not in config:
        print("Missing slack in config")
        sys.exit(0)

    slackbot = Bot(config)

    try:
        slackbot.start()
    except KeyboardInterrupt:
        slackbot.quit()


if __name__ == '__main__':
    run()
