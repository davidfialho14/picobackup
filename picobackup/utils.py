import contextlib


@contextlib.contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
