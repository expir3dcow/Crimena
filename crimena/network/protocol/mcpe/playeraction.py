from crimena.network.protocol.packet import Packet


class PlayerAction(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        action = self.get_int()
        x = self.get_int()
        y = self.get_int()
        z = self.get_int()
        face = self.get_int()
        entity_id = self.get_int()

        self.debug.append(['action', action])
        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['face', face])
        self.debug.append(['entity_id', entity_id])


def init(data):
    return PlayerAction(data)


def info():
    return {'pid': 164}