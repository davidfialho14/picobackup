import contextlib
import os
import socket
import xmlrpclib
from os import path
from time import sleep

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from picobackup.data_format import encode
from picobackup.push_directory import PushDirectory
from picobackup.push_file import PushFile
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
            if path.isdir(event.src_path):
                self._pusher.push(PushDirectory(event.src_path))
            elif path.isfile(event.src_path):
                self._pusher.push(PushFile(event.src_path))

    # --- PUBLIC INTERFACE --- #

    def __init__(self, server_address, watch_dir):
        self.server_address = server_address
        self.watch_dir = watch_dir
        self.server = xmlrpclib.ServerProxy(self.server_address)

    def push(self, push_item):
        """
        Pushes any push be it a file or a directory. It blocks until it can
        push the item

        :param push_item: item to be pushed.
        """
        pushed = False
        while not pushed:
            try:
                push_item.push(self.server, self.watch_dir)
                pushed = True
            except socket.error:
                print "could not push not will try later"
                sleep(5)

    def serve_forever(self):
        """ Watches a directory an pushes new files forever """
        self.__push_watch_dir()
        self.__start_watcher()
        sleep_forever()

    # --- END PUBLIC INTERFACE --- #

    def __push_watch_dir(self):
        for root, dirs, files in os.walk(self.watch_dir):
            for file in files:
                self.push(PushFile(path.join(root, file)))

    def __start_watcher(self):
        observer = Observer()
        observer.schedule(Pusher.FolderHandler(self), self.watch_dir,
                          recursive=True)
        observer.start()
