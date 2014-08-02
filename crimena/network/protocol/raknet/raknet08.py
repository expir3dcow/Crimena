from crimena.network.protocol.packet import Packet


class Raknet08(Packet):
    """ID_OPEN_CONNECTION_REPLY_2
    Structure
        packet id: byte
        magic: 16 bytes
        server_id: long
        client_port: short
        mtu_size: short
        security: byte
    """

    client_port = None
    mtu_size = None
    magic = None

    def __init__(self, server):
        Packet.__init__(self, server)

    def encode(self):
        self.put_pid()
        self.put_magic()
        self.put_serverid()
        self.put_short(self.client_port)
        self.put_short(self.mtu_size)
        self.put_byte(0)

    def decode(self):
        pass

    def pid(self):
        return 8