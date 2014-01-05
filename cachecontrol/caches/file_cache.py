import os
import base64

try:
    from cPickle import load, dump
except ImportError:
    from pickle import load, dump

from lockfile import FileLock


class FileCache(object):

    def __init__(self, directory, forever=False):
        self.directory = directory
        self.forever = forever

        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)

    def encode(self, x):
        return base64.b64encode(x.encode("UTF-8")).decode("ascii")

    def _fn(self, name):
        return os.path.join(self.directory, self.encode(name))

    def get(self, key):
        name = self._fn(key)
        if os.path.exists(name):
            return load(open(name))

    def set(self, key, value):
        name = self._fn(key)
        lock = FileLock(name)
        with lock:
            with open(lock.path, 'w+') as fh:
                dump(value, fh)

    def delete(self, key):
        if not self.forever:
            os.remove(self._fn(key))
