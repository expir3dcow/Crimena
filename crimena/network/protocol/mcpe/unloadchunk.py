from crimena.network.protocol.packet import Packet


class UnloadChunk(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        x = self.get_int()
        z = self.get_int()

        self.debug.append(['x', x])
        self.debug.append(['z', z])


def init(data):
    return UnloadChunk(data)


def info():
    return {'pid': 187}