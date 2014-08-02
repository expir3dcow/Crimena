from crimena.network.protocol.packet import Packet


class RakNet06(Packet):

    magic = None
    server_id = None
    security = 0
    mtu_size = None

    def __init__(self):
        Packet.__init__(self)

    def decode(self):
        pass

    def encode(self):
        self.put_byte(self.get_pid())
        self.put_magic(self.magic)
        self.put_long(self.server_id)
        self.put_byte(self.security)
        self.put_short(self.mtu_size)

    def get_pid(self):
        return 6

