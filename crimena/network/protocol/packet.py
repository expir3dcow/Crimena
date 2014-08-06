import abc

from crimena.utils import binutils


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

    def __tostr__(self):
        return self.__name__

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
        return binutils.get_byte(self.get(1))

    def put_byte(self, i):
        self.buffer.extend(binutils.put_byte(i))

    def get_short(self):
        return binutils.get_short(self.get(2))

    def put_short(self, i):
        self.buffer.extend(binutils.put_short(i))

    def get_long(self):
        return binutils.get_long(self.get(8))

    def put_long(self, i):
        self.buffer.extend(binutils.put_long(i))

    def get_magic(self):
        return self.get(16)

    def put_magic(self):
        self.buffer.extend(self.magic)

    def get_string(self):
        length = binutils.get_short(self.get(2))
        return binutils.get_short(self.get(length))

    def put_string(self, i):
        self.buffer.extend(binutils.put_string(i))

    # Custom stuff
    def put_pid(self):
        self.put_byte(self.pid())

    def put_serverid(self):
        self.put_long(self.server.server_id)

    def put_server_pingid(self):
        self.buffer.extend(binutils.put_long(self.server.get_time_since_start()))

    def put_server_identifier(self):
        self.buffer.extend(binutils.put_string("MCCPP;Demo;Crimena"))  # TODO: load from config