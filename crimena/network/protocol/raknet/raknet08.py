"""Packet info
    name=ID_OPEN_CONNECTION_REPLY_2
    pid=8
"""

from crimena.network.protocol.packet import Packet


class Raknet08(Packet):
    """Packet structure
        packet_id: byte
        magic: 16 bytes
        server_id: long
        client_port: short
        mtu_size: short
        security: byte
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.client_port = None
        self.mtu_size = None
        self.magic = None

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


def init(server):
    return Raknet08(server)