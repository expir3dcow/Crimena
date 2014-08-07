from crimena.network.protocol.packet import Packet


class EntityData(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        x = self.get_int()
        y = self.get_byte()
        z = self.get_int()
        namedtag = self.get()

        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        # self.debug.append(['namedtag', namedtag])  # FIXME: make it work


def init(data):
    return EntityData(data)


def info():
    return {'pid': 184}