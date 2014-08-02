from crimena.network.protocol.packet import Packet


class RakNet05(Packet):

    magic = None
    protocol_version = None
    mtu_size = None

    def __init__(self):
        Packet.__init__(self)

    def decode(self):
        self.get(1)
        self.magic = self.get_magic()
        self.protocol_version = self.get_byte()
        self.mtu_size = len(self.get())

    def encode(self):
        pass
