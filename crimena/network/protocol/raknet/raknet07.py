from crimena.network.protocol.packet import Packet


class Raknet07(Packet):
    """ID_OPEN_CONNECTION_REQUEST_2
    Structure
        packet id: byte
        magic: 16 bytes
        security: byte
        cookie: 4 bytes
        server_port: short
        mtu_size: short
        client_id: long
    """

    magic = None
    security = None
    cookie = None
    server_port = None
    mtu_size = None
    client_id = None

    def __init__(self, server):
        Packet.__init__(self, server)

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

    def pid(self):
        return 7

    def reply(self):
        return [8]