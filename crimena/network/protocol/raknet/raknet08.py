from crimena.network.protocol.packet import Packet

info = {
        'pid': 8,
        'fields': ['magic', 'mtu_size'],
    }


class Raknet08(Packet):
    """ID_OPEN_CONNECTION_REPLY_2
        packet_id:  Header(1)
        magic:      OfflineMesageID(16)
        server_id:  server GUID(8)
        lient_port: mtu(2)
        security:   doSecurity(1 bit)
            handshakeAnswer (if do security is true).
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