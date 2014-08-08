from crimena.network.protocol.packet import Packet

info = {
        'pid': 7,
        'reply': [8],
        'fields': ['magic', 'mtu_size'],
    }


class Raknet07(Packet):
    """Packet structure
        packet_id:      Header(1)
        magic:          OfflineMesageID(16)
        cookie:         Cookie(4, if HasSecurity is true on the server)
        security:       clientSupportsSecurity(1 bit)
            # not used: handshakeChallenge (if has security on both server and client)
        server_port:    remoteBindingAddress(6)
        mtu_size:       MTU(2)
        client_id:      client GUID(8)

        Connection slot allocated if
            cookie is valid,
            server is not full,
            GUID and IP not already in use.
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.magic = None
        self.cookie_security = None
        self.server_port = None
        self.mtu_size = None
        self.client_id = None

    def encode(self):
        pass

    def decode(self):
        self.get(1)
        self.magic = self.get_magic()
        self.cookie_security = self.get(5)
        self.server_port = self.get_short()
        self.mtu_size = self.get_short()
        self.client_id = self.get_long()


def init(server):
    return Raknet07(server)