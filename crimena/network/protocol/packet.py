import abc
from struct import unpack, pack


class Packet(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.buffer = bytearray()

    @abc.abstractmethod
    def encode(self):
        pass

    @abc.abstractmethod
    def decode(self):
        pass

    @abc.abstractproperty
    def get_pid(self):
        return None

    def get(self, length=-1):
        if length > 0:
            r = self.buffer[:length]
            self.buffer = self.buffer[length:]
            return r
        else:
            r = self.buffer
            self.buffer = bytearray()
            return r

    def get_byte(self):
        return unpack('>B', self.get(1))[0]

    def get_long(self):
        return unpack('>Q', self.get(8))[0]

    def get_magic(self):
        return unpack('>16s', self.get(16))[0]

    def put_byte(self, i):
        self.buffer.extend(pack('>B',i))

    def put_short(self, i):
        self.buffer.extend(pack('>H', i))

    def put_long(self, i):
        self.buffer.extend(pack('>Q', i))

    def put_magic(self, i):
        self.buffer.extend(i)

    def put_string(self, i):
        self.put_short(len(i))
        self.buffer.extend(i.encode())




