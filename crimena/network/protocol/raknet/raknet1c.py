from crimena.network.protocol.packet import Packet


class Raknet1c(Packet):
    """ID_UNCONNECTED_PING_OPEN_CONNECTIONS
    Structure
        packet id: byte
        ping_id: long
        server_id: long
        magic: 16 bytes
        identifier: string
    """

    ping_id = None
    magic = None

    def __init__(self, server):
        Packet.__init__(self, server)

    def encode(self):
        self.put_byte(self.pid())
        self.put_server_pingid()
        self.put_serverid()
        self.put_magic()
        self.put_server_identifier()

    def decode(self):
        pass

    def pid(self):
        return 28