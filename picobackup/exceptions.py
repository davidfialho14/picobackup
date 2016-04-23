
class FileExistsError(OSError):
    """ Raised to indicate that a file exists """

    def __init__(self, file_path):
        super(FileExistsError, self).__init__(
            FileExistsError, "file '%s' already exists" % file_path)
