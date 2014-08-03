"""Packet info
    name=ID_OPEN_CONNECTION_REQUEST_1
    pid=5
    reply=6
"""

from crimena.network.protocol.packet import Packet


class Raknet05(Packet):
    """Packet structure
        packet_id: byte
        magic: 16 bytes
        protocol_version: byte
        mtu_size: short
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.magic = None
        self.protocol_version = None
        self.mtu_size = None

    def encode(self):
        pass

    def decode(self):
        self.get(1)
        self.magic = self.get_magic()
        self.protocol_version = self.get_byte()
        self.mtu_size = len(self.get())

    def pid(self):
        return 5


def init(server):
    return Raknet05(server)