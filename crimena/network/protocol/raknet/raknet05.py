from crimena.network.protocol.packet import Packet


class Raknet05(Packet):
    """ID_OPEN_CONNECTION_REQUEST_1
    Structure
        packet id: byte
        magic: 16 bytes
        protocol_version: byte
        mtu_size: size of rest of data
    """

    magic = None
    protocol_version = None
    mtu_size = None

    def __init__(self, server):
        Packet.__init__(self, server)

    def encode(self):
        pass

    def decode(self):
        self.get(1)
        self.magic = self.get_magic()
        self.protocol_version = self.get_byte()
        self.mtu_size = len(self.get())

    def pid(self):
        return 5

    def reply(self):
        return [6]