import base64


def encode(data):
    """
    Encodes the data structure to a format that can be pushed.

    :param data: data structure obtained from the rsync delta.
    :return: data structured encoded.
    """
    encoded_data = [data[0]]  # the first item is the block size
    for block in data[1:]:  # skip block size
        encoded_data.append(base64.b64encode(block))

    return encoded_data


def decode(data):
    """
    Decodes the data structure from the push format to the foramt that rsync
    expects.

    :param data: data structure obtained from the rsync delta.
    :return: data structured encoded.
    """
    decoded_data = [data[0]]  # the first item is the block size
    for block in data[1:]:  # skip block size
        decoded_data.append(base64.b64decode(block))

    return decoded_data
