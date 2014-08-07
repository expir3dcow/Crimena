from crimena.network.protocol.packet import Packet

info = {'pid': 187}


class UnloadChunk(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.x = None
        self.z = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.x)
        self.put_int(self.z)

    def decode(self):
        x = self.get_int()
        z = self.get_int()


def init(data):
    return UnloadChunk(data)