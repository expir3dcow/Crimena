from crimena.network.protocol.packet import Packet


class Explode(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        x = self.get_float()
        y = self.get_float()
        z = self.get_float()
        radius = self.get_float()
        records = self.get_int()
        if records > 0:
            for i in range(0, records):
                rx = self.get_byte()
                ry = self.get_byte()
                rz = self.get_byte()

        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['radius', radius])
        self.debug.append(['records', records])


def init(data):
    return Explode(data)


def info():
    return {'pid': 154}