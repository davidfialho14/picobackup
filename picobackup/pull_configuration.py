import os

from configparser import ConfigParser
from os import path

from picobackup import defaults
from picobackup.configuration import Configuration
from picobackup.exceptions import ConfigError
from picobackup.utils import ignored


class PullConfiguration(Configuration):

    def __init__(self):
        self._config_file = defaults.pull_config_file
        super(PullConfiguration, self).__init__(self._config_file)
