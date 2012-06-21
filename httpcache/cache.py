"""
The cache object API for implementing caches. The default is just a
dictionary, which in turns means it is not threadsafe for writing.
"""


class BaseCache(object):

    def get(self, key):
        raise NotImplemented()

    def set(self, key, value):
        raise NotImplemented()

    def delete(self, key):
        raise NotImplemented()


class DictCache(BaseCache):

    def __init__(self, init_dict=None):
        self.data = init_dict or {}

    def get(self, key):
        return self.data.get(key, None)

    def set(self, key, value):
        self.data.update({key: value})

    def delete(self, key):
        self.data.pop(key)