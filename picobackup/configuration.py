import os

from configparser import ConfigParser
from os import path

from picobackup.exceptions import ConfigError
from picobackup.utils import ignored


class Configuration(object):
    """
    Implements an abstraction to access the configuration file parameters
    """

    def __init__(self, file_path):
        self.file_path = file_path
        config = ConfigParser()

        if not path.isfile(self.file_path):
            # create the config file
            with open(self.file_path, "w+") as config_file:
                config_file.write("[DEFAULT]\n")

        config.read(self.file_path)
        try:
            self._config = config['DEFAULT']
        except KeyError:
            raise ConfigError("configuration file is corrupted")

    @property
    def directory(self):
        try:
            return self._config['directory']
        except KeyError:
            return None

    @directory.setter
    def directory(self, value):
        if not path.isdir(value):
            raise ConfigError("directory '%s' does not exist" % value)

        self.__save_configuration(config_name='directory', value=value)

    @property
    def host(self):
        try:
            return self._config['host']
        except KeyError:
            return None

    @host.setter
    def host(self, value):
        self.__save_configuration(config_name='host', value=value)

    @property
    def port(self):
        try:
            return int(self._config['port'])
        except KeyError:
            return None

    @port.setter
    def port(self, value):

        if not value.isdigit() or not (0 <= int(value) < 65536):
            raise ConfigError("port must be an integer between 0 and 65535")

        self.__save_configuration(config_name='port', value=value)

    def clear(self):
        with ignored(OSError):  # ignore if file does not exist
            os.remove(self.file_path)

        self._config = dict()

    def __save_configuration(self, config_name, value):
        with open(self.file_path, "a") as config_file:
            config_file.write("%s: %s\n" % (config_name, str(value)))

        self._config[config_name] = value

