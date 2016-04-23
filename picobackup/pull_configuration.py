import os

from configparser import ConfigParser
from os import path

from picobackup.configuration import Configuration
from picobackup.exceptions import ConfigError
from picobackup.utils import ignored


class PullConfiguration(Configuration):

    def __init__(self):
        self._config_file = 'pull.conf'
        super(PullConfiguration, self).__init__(self._config_file)
