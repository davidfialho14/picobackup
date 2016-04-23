import logging
import os.path as path


class PushDirectory:
    """ Represents a directory to be pushed """

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def push(self, server, watch_dir):
        logging.debug("trying to push directory: %s" % self.dir_path)
        server.push_dir(path.relpath(self.dir_path, watch_dir))
        logging.info("pushed directory: %s" % self.dir_path)
