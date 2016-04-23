
class Pusher:
    """ Pusher watches a directory and pushes all new created files """

    def __init__(self, server_address, watch_dir):
        self.server_address = server_address
        self.watch_dir = watch_dir

    def serve_forever(self):
        """ Watches a directory an pushes new files forever """
        pass
