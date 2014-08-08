from crimena.network.protocol.packet import Packet

info = {
        'pid': 5,
        'reply': [6],
        'fields': ['magic', 'protocol_version', 'mtu_size'],
    }


class Raknet05(Packet):
    """ID_OPEN_CONNECTION_REQUEST_1
        packet_id:          Header(1)
        magic:              OfflineMesageID(16)
        protocol_version:   Protocol number(1)
        mtu_size:           Pad(toMTU)

        sent with no fragment set.
        If protocol fails on server,
            returns ID_INCOMPATIBLE_PROTOCOL_VERSION to client
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.magic = None
        self.protocol_version = None
        self.mtu_size = None

    def encode(self):
        pass

    def decode(self):
        self.get(1)
        self.magic = self.get_magic()
        self.protocol_version = self.get_byte()
        self.mtu_size = len(self.get())


def init(server):
    return Raknet05(server)