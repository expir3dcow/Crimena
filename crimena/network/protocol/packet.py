import abc
from struct import unpack, pack


class Packet(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, server):
        self.buffer = bytearray()
        self.server = server

    @abc.abstractmethod
    def encode(self):
        """Encode data before sending"""
        pass

    @abc.abstractmethod
    def decode(self):
        """Decode received data"""
        pass

    @abc.abstractmethod
    def pid(self):
        """Returns the packet ID"""
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

    def put_byte(self, i):
        self.buffer.extend(pack('>B', i))

    def get_short(self):
        return unpack('>H', self.get(2))[0]

    def put_short(self, i):
        self.buffer.extend(pack('>H', i))

    def get_long(self):
        return unpack('>Q', self.get(8))[0]

    def put_long(self, i):
        self.buffer.extend(pack('>Q', i))

    def get_magic(self):
        return unpack('>16s', self.get(16))[0]

    def put_magic(self):
        self.buffer.extend(self.magic)

    def get_string(self):
        return self.get(self.get_short())

    def put_string(self, i):
        self.put_short(len(i))
        self.buffer.extend(i.encode())

    # Custom stuff
    def put_pid(self):
        self.put_byte(self.pid())

    def put_serverid(self):
        self.put_long(self.server.server_id)

    def put_server_pingid(self):
        self.put_long(self.server.get_time_since_start())

    def put_server_identifier(self):
        self.put_string("MCCPP;Demo;Crimena")  # TODO: load from config