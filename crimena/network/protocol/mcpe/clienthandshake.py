from crimena.network.protocol.packet import Packet

info = {'pid': 19}


class ClientHandshake(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.security = None
        self.cookie = None
        self.client_port = None
        self.data_array = None
        self.timestamp = None
        self.session1 = None
        self.session2 = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.security)
        self.put_int(self.cookie)
        self.put_short(self.client_port)
        self.put(self.data_array)
        self.put(b'\x00\x00\x04\xff\xff\xff\xff'*9)  # TODO: test if this works
        self.put_short(self.timestamp)
        self.put_long(self.session2)
        self.put_long(self.session1)

    def decode(self):
        self.security = self.get_byte()
        self.cookie = self.get_int()
        self.client_port = self.get_short()
        self.data_array = self.get(self.get_byte())
        for i in range(0, 9):
            self.get(3)
            self.get(4)
        self.timestamp = self.get_short()
        self.session2 = self.get_long()
        self.session1 = self.get_long()


def init(data):
    return ClientHandshake(data)