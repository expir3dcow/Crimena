from crimena.network.protocol.packet import Packet

info = {
        'pid': 6,
        'fields': ['magic', 'mtu_size'],
    }


class Raknet06(Packet):
    """ID_OPEN_CONNECTION_REPLY_1
    packet_id:  Header(1)
    magic:      OfflineMesageID(16)
    server_id:  server GUID(8)
    security:   HasSecurity(1)
    mtu_size:   MTU(2).

    If public key fails on client
        returns ID_PUBLIC_KEY_MISMATCH
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.magic = None
        self.mtu_size = None

    def encode(self):
        self.put_byte(info['pid'])
        self.put_magic()
        self.put_serverid()
        self.put_byte(0)
        self.put_short(self.mtu_size)

    def decode(self):
        pass


def init(server):
    return Raknet06(server)