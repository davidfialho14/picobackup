
class PushServer:
    """ Simple push server to backup files to a directory """

    def __init__(self, address, base_dir):
        self.address = address
        self.base_dir = base_dir

    def push(self, file_path, data):
        """
        Pushes a new file to the server. The file_path is the path to store
        the new file and it is relative to the base directory of the server.

        :param file_path: path where to store the file (relative to base
        directory)
        :param data: pushed data to be stored.
        """
        pass

    def serve_forever(self):
        """ Listens for new pushes forever """
        pass


class PushServerInterface:
    """ Defines the public interface of the push server """

    def __init__(self, push_server):
        """
        Associates the push server interface with the given push server.

        :param push_server: server to associate with the interface.
        """
        self.push_server = push_server  # type: PushServer

    def push(self, file_path, data):
        """ see PushServer.push method """
        self.push_server.push(file_path, data)
