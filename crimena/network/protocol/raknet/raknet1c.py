from crimena.network.protocol.packet import Packet

info = {
        'pid': 28,
        'fields': ['magic'],
    }


class Raknet1c(Packet):
    """Packet structure
        packet_id: Header(1)
        ping_id: client GUID(8)
        server_id: server GUID(8)
        magic: OfflineMesageID(16)
        identifier: string
    """

    def __init__(self, server):
        Packet.__init__(self, server)
        self.ping_id = None
        self.magic = None

    def encode(self):
        self.put_byte(info['pid'])
        self.put_server_pingid()
        self.put_serverid()
        self.put_magic()
        self.put_server_identifier()

    def decode(self):
        pass


def init(server):
    return Raknet1c(server)