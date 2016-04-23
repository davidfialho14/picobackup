import logging
import os
import os.path as path

import pyrsync as rsync
from picobackup.data_format import encode


class PushFile:
    """ Represents a file to be pushed """

    empty_hashes = ([], [])  # hashes for an empty file

    def __init__(self, file_path):
        self.file_path = file_path

    def push(self, server, watch_dir):
        with open(self.file_path, "rb") as created_file:
            data = rsync.rsyncdelta(created_file, PushFile.empty_hashes)

        logging.debug("trying to push file: %s" % self.file_path)
        server.push(path.relpath(self.file_path, watch_dir), encode(data))
        logging.info("pushed file: %s" % self.file_path)

        os.remove(self.file_path)
        logging.debug("removed file: %s" % self.file_path)
