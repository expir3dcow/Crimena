from crimena.network.protocol.packet import Packet


class UpdateBlock(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        x = self.get_int()
        z = self.get_int()
        y = self.get_byte()
        block = self.get_byte()
        meta = self.get_byte()

        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['block', block])
        self.debug.append(['meta', meta])


def init(data):
    return UpdateBlock(data)


def info():
    return {'pid': 152}