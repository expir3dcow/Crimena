from crimena.network.protocol.packet import Packet


class RakNet1c(Packet):

    ping_id = None
    server_id = None
    magic = None
    identifier = None

    def __init__(self):
        Packet.__init__(self)

    def decode(self):
        pass

    def encode(self):
        self.put_byte(self.get_pid())
        self.put_long(self.ping_id)
        self.put_long(self.server_id)
        self.put_magic(self.magic)
        self.put_string(self.identifier)

    def get_pid(self):
        return 28


