from crimena.network.protocol.packet import Packet


class Raknet01(Packet):
    """ID_CONNECTED_PING_OPEN_CONNECTIONS
    Structure
        packet id: byte
        ping_id: long
        magic: 16 bytes
    """

    ping_id = None
    magic = None

    def __init__(self, server):
        Packet.__init__(self, server)

    def encode(self):
        pass

    def decode(self):
        self.get(1)
        self.ping_id = self.get_long()
        self.magic = self.get_magic()

    def pid(self):
        return 1

    def reply(self):
        return [28]