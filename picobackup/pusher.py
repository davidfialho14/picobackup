import os
import xmlrpclib

from os import path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import pyrsync as rsync
from picobackup.data_format import encode
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

    empty_hashes = ([], [])  # hashes for an empty file

    def __init__(self, server_address, watch_dir):
        self.server_address = server_address
        self.watch_dir = watch_dir

    def push(self, file_path):
        """
        Pushes a file to the push server on the address provided on
        initialization.

        :param file_path: path to the file to push (including the watch
        directory).
        """
        print "pushed: %s" % file_path

        # connect to the server
        server = xmlrpclib.ServerProxy(self.server_address)

        self.__send_file(server, file_path)
        os.remove(file_path)

    def serve_forever(self):
        """ Watches a directory an pushes new files forever """
        self.__start_watcher()

    def __start_watcher(self):
        observer = Observer()
        observer.schedule(Pusher.FolderHandler(self), self.watch_dir,
                          recursive=True)
        observer.start()
        sleep_forever()

    def __send_file(self, server, file_path):
        with open(file_path, "rb") as created_file:
            data = rsync.rsyncdelta(created_file, Pusher.empty_hashes)

        server.push(path.relpath(file_path, self.watch_dir), encode(data))
