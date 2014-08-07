from crimena.network.protocol.packet import Packet


class TileEvent(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        x = self.get_int()
        y = self.get_int()
        z = self.get_int()
        case1 = self.get_int()
        case2 = self.get_int()

        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['case1', case1])
        self.debug.append(['case2', case2])


def init(data):
    return TileEvent(data)


def info():
    return {'pid': 156}