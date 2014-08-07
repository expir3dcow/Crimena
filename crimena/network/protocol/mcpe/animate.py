from crimena.network.protocol.packet import Packet


class Animate(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        action = self.get_byte()
        entity_id = self.get_int()

        self.debug.append(['action', action])
        self.debug.append(['entity_id', entity_id])


def init(data):
    return Animate(data)


def info():
    return {'pid': 172}