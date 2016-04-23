"""Picobackup
Usage:
  picobackup.py start [pull | push ]
  picobackup.py (-h | --help)

Options:
  -h --help         Show this screen.
  --version         Show version.
  --config=<file>   Uses the specified configuration file

"""
from docopt import docopt

from picobackup.configuration import Configuration
from picobackup.push_server import PushServer
from picobackup.pusher import Pusher

config_file = '../config.conf'


def setup_configuration():
    print "CONFIGURATIONS"
    configuration = Configuration(config_file)

    if configuration.directory:
        print "directory: %s" % configuration.directory
    else:
        configuration.directory = raw_input("directory: ")

    if configuration.host:
        print "host: %s" % configuration.host
    else:
        configuration.host = raw_input("host: ")

    if configuration.port:
        print "port: %s" % configuration.port
    else:
        configuration.port = raw_input("port: ")

    return configuration


def main():
    args = docopt(__doc__, version='Picobackup Version 1.0')

    config = setup_configuration()

    if args['push']:
        server_address = 'http://%s:%s' % (config.host, config.port)
        service = Pusher(server_address, config.directory)
    else:
        service = PushServer((config.host, int(config.port)), config.directory)

    service.serve_forever()


if __name__ == '__main__':
    main()
