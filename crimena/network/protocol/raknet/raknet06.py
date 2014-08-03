"""Packet info
    name=ID_OPEN_CONNECTION_REPLY_1
    pid=6
"""

from crimena.network.protocol.packet import Packet


class Raknet06(Packet):
    """Packet structure
        packet_id: byte
        magic: 16 bytes
        server_id: long
        security: byte
        mtu_size: short
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.magic = None
        self.mtu_size = None

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


def init(server):
    return Raknet06(server)