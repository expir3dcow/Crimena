from crimena.network.protocol.packet import Packet


class Respawn(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        x = self.get_float()
        y = self.get_float()
        z = self.get_float()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])


def init(data):
    return Respawn(data)


def info():
    return {'pid': 173}