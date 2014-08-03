"""Packet info
    name=ID_CONNECTED_PING_OPEN_CONNECTIONS
    pid=1
    reply=28
"""

from crimena.network.protocol.packet import Packet


class Raknet01(Packet):
    """Packet structure
        packet_id: byte
        ping_id: long
        magic: 16 bytes
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.ping_id = None
        self.magic = None

    def encode(self):
        pass

    def decode(self):
        self.get(1)
        self.ping_id = self.get_long()
        self.magic = self.get_magic()

    def pid(self):
        return 1


def init(server):
    return Raknet01(server)