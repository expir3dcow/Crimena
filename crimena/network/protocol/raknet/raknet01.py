from crimena.network.protocol.packet import Packet


class RakNet01(Packet):

    ping_id = None
    magic = None

    def __init__(self):
        Packet.__init__(self)

    def encode(self):
        pass

    def decode(self):
        self.get(1)
        self.ping_id = self.get_long()
        self.magic = self.get_magic()