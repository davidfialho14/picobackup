"""Picobackup
Usage:
  picobackup.py start ( pull | push )
  picobackup.py clear ( pull | push )
  picobackup.py (-h | --help)

Options:
  -h --help         Show this screen.
  --version         Show version.

"""

from docopt import docopt

import logging

from picobackup import defaults
from picobackup.pull_configuration import PullConfiguration
from picobackup.push_configuration import PushConfiguration
from picobackup.push_server import PushServer
from picobackup.pusher import Pusher


def setup_configuration(configuration):
    print "CONFIGURATIONS"

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

    logging.info("set configurations: %s" % configuration)

    return configuration


def main():
    args = docopt(__doc__, version='Picobackup Version 1.0')

    logging.basicConfig(filename=defaults.log_file, level=logging.DEBUG)

    if args['clear']:
        if args['push']:
            logging.info("Running clear push")
            PushConfiguration().clear()
            logging.info("Cleared push configurations")
        else:
            logging.info("Running clear pull")
            PullConfiguration().clear()
            logging.info("Cleared pull configurations")

        print "cleared configurations successfully"

    elif args['start']:
        if args['push']:
            logging.info("Running as PUSH service")

            config = setup_configuration(PushConfiguration())
            server_address = 'http://%s:%d' % (config.host, config.port)
            service = Pusher(server_address, config.directory)
        else:
            logging.info("Running as PULL service")

            config = setup_configuration(PullConfiguration())
            service = PushServer((config.host, config.port),
                                 config.directory)
        try:
            service.serve_forever()
        except KeyboardInterrupt:
            pass

    logging.info("Exited correctly")

if __name__ == '__main__':
    main()
