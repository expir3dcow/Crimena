from crimena.network.protocol.packet import Packet


class EntityEvent(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        event = self.get_byte()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['event', event])


def init(data):
    return EntityEvent(data)


def info():
    return {'pid': 157}