from crimena.network.protocol.packet import Packet


class TakeItemEntity(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        target = self.get_int()
        entity_id = self.get_int()

        self.debug.append(['target', target])
        self.debug.append(['entity_id', entity_id])


def init(data):
    return TakeItemEntity(data)


def info():
    return {'pid': 143}