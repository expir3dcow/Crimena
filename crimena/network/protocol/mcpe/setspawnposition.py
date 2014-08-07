from crimena.network.protocol.packet import Packet


class SetSpawnPosition(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        x = self.get_int()
        z = self.get_int()
        y = self.get_byte()

        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])


def init(data):
    return SetSpawnPosition(data)


def info():
    return {'pid': 171}