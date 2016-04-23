from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from picobackup.utils import sleep_forever


class Pusher:
    """ Pusher watches a directory and pushes all new created files """

    class FolderHandler(FileSystemEventHandler):
        """
        Listens for new created files and calls the push method for each
        new file.
        """
        def __init__(self, pusher):
            self._pusher = pusher  # type: Pusher

        def on_created(self, event):
            self._pusher.push(event.src_path)

    def __init__(self, server_address, watch_dir):
        self.server_address = server_address
        self.watch_dir = watch_dir

    def push(self, file_path):
        print "pushed: %s" % file_path

    def serve_forever(self):
        """ Watches a directory an pushes new files forever """
        observer = Observer()
        observer.schedule(Pusher.FolderHandler(self), self.watch_dir,
                          recursive=True)
        observer.start()
        sleep_forever()
