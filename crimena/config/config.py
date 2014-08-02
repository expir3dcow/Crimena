import os
import abc


class Config(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.data = {}

    def file_exists(self):
        """Check if file exists
              if not then create it
        """
        if not os.path.isfile(self.filename):
            open(self.filename, 'w').close()

    @abc.abstractmethod
    def load(self):
        pass

    @abc.abstractmethod
    def save(self):
        pass

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value