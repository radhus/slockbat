import sys


def parse_config(path):
    import configparser
    import os

    config = configparser.ConfigParser()

    res = config.read(os.path.realpath(path))
    if len(res) == 0:
        print('Missing config file.')
        sys.exit(0)

    return config
