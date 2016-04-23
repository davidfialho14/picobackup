import os

from picobackup.utils import ignored


def create_dirs(file_path):
    """
    Creates where the file should be stored. If the directories already exist
    nothing happens.

    :param file_path: path to the file
    """
    dirs, filename = os.path.split(file_path)

    with ignored(OSError):  # ignore if the directory already exists
        os.makedirs(dirs, mode=0755)
