import time
from crimena.config.config import Config


class Properties(Config):
    """Properties config

    Fileformat:
    normal text file
    with key=value format
    """

    def __init__(self, filename):
        Config.__init__(self)
        self.filename = filename
        self.file_exists()
        pass

    def load(self):
        with open(self.filename, 'r') as f:
            for line in f:
                if not line.startswith('#'):
                    k, v = line.strip().split('=')
                    self.data[k] = self.data.get(k, v)

    def save(self):
        with open(self.filename, 'w') as f:
            f.write('# Created on {}\n'.format(time.strftime("%c")))
            for k, v in self.data.items():
                f.write('{key}={value}\n'.format(key=k, value=v))

    def get(self, key, default):
        self.data[key] = self.data.get(key, default)
        return self.data[key]
