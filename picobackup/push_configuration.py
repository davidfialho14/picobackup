import os

from configparser import ConfigParser
from os import path

from picobackup import defaults
from picobackup.configuration import Configuration
from picobackup.exceptions import ConfigError
from picobackup.utils import ignored


class PushConfiguration(Configuration):
    """
    Implements an abstraction to access the configuration file parameters
    """

    def __init__(self):
        self._config_file = defaults.push_config_file
        super(PushConfiguration, self).__init__(self._config_file)
