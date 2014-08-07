from crimena.network.protocol.packet import Packet

info = {'pid': 16}


class ServerHandshake(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.security = None
        self.cookie = None
        self.port = None
        self.session1 = None
        self.session2 = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.security)
        self.put_int(self.cookie)
        self.put_short(self.port)
        self.put(b'\x00\x00\x04\xff\xff\xff\xff'*10)
        self.put_byte(1)
        self.put_long(self.session1)
        self.put_long(self.session2)

    def decode(self):
        self.security = self.get_byte()
        self.cookie = self.get_int()
        self.port = self.get_short()
        for i in range(0, 10):
            self.get(3)
            self.get(4)
        self.get(1)
        self.session1 = self.get_long()
        self.session2 = self.get_long()


def init(data):
    return ServerHandshake(data)