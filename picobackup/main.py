"""Picobackup
Usage:
  picobackup.py start ( pull | push )
  picobackup.py clear ( pull | push )
  picobackup.py (-h | --help)

Options:
  -h --help         Show this screen.
  --version         Show version.
  --config=<file>   Uses the specified configuration file

"""

from docopt import docopt

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

    return configuration


def main():
    args = docopt(__doc__, version='Picobackup Version 1.0')

    if args['clear']:
        if args['push']:
            PushConfiguration().clear()
        else:
            PullConfiguration().clear()
        print "cleared configurations successfully"

    elif args['start']:
        if args['push']:
            config = setup_configuration(PushConfiguration())
            server_address = 'http://%s:%d' % (config.host, config.port)
            service = Pusher(server_address, config.directory)
        else:
            config = setup_configuration(PullConfiguration())
            service = PushServer((config.host, config.port),
                                 config.directory)
        try:
            service.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
