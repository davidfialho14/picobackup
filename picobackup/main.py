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

from picobackup.push_server import PushServer
from picobackup.pusher import Pusher


def main():
    args = docopt(__doc__, version='Picobackup Version 1.0')

    if args['push']:
        service = Pusher('http://localhost:5000', '../experiments/client')
    else:
        service = PushServer(('localhost', 5000), '../experiments/server')

    service.serve_forever()


if __name__ == '__main__':
    main()
