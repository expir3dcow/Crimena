from crimena.network.protocol.packet import Packet


class Raknet06(Packet):
    """ID_OPEN_CONNECTION_REPLY_1
    Structure
        packet id: byte
        magic: 16 bytes
        server_id: long
        security: byte
        mtu_size: short
    """

    magic = None
    mtu_size = None

    def __init__(self, server):
        Packet.__init__(self, server)

    def encode(self):
        self.put_pid()
        self.put_magic()
        self.put_serverid()
        self.put_byte(0)
        self.put_short(self.mtu_size)

    def decode(self):
        pass

    def pid(self):
        return 6