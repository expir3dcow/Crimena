from crimena.network.protocol.packet import Packet

info = {
        'pid': 7,
        'reply': [8],
        'fields': ['magic', 'mtu_size'],
    }


class Raknet07(Packet):
    """Packet structure
        packet_id: byte
        magic: 16 bytes
        security: byte
        cookie: 4 bytes
        server_port: short
        mtu_size: short
        client_id: long
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.magic = None
        self.security = None
        self.cookie = None
        self.server_port = None
        self.mtu_size = None
        self.client_id = None

    def encode(self):
        pass

    def decode(self):
        self.get(1)
        self.magic = self.get_magic()
        self.security = self.get_byte()
        self.cookie = self.get(4)
        self.server_port = self.get_short()
        self.mtu_size = self.get_short()
        self.client_id = self.get_long()


def init(server):
    return Raknet07(server)