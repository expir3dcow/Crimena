from crimena.network.protocol.packet import Packet


class RemoveEntity(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()

        self.debug.append(['entity_id', entity_id])


def init(data):
    return RemoveEntity(data)


def info():
    return {'pid': 141}