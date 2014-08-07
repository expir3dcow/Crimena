from crimena.network.protocol.packet import Packet

info = {
        'pid': 8,
        'fields': ['magic', 'mtu_size'],
    }


class Raknet08(Packet):
    """Packet structure
        packet_id: byte
        magic: 16 bytes
        server_id: long
        client_port: short
        mtu_size: short
        security: byte
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.client_port = None
        self.mtu_size = None
        self.magic = None

    def encode(self):
        self.put_byte(info['pid'])
        self.put_magic()
        self.put_serverid()
        self.put_short(self.client_port)
        self.put_short(self.mtu_size)
        self.put_byte(0)

    def decode(self):
        pass


def init(server):
    return Raknet08(server)