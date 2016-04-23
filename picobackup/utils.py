import contextlib

import time


@contextlib.contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


def sleep_forever():
    while True:
        time.sleep(10000)
