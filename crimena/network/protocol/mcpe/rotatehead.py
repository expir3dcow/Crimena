from crimena.network.protocol.packet import Packet


class RotateHead(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_count = self.get_int()
        for i in range(0, entity_count):
            entity_id = self.get_int()
            entity_rotation = self.get_byte()/360
        self.debug.append(['entity_count', entity_count])


def init(data):
    return RotateHead(data)


def info():
    return {'pid': 148}