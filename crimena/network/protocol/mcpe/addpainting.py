from crimena.network.protocol.packet import Packet


class AddPainting(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        x = self.get_int()
        y = self.get_int()
        z = self.get_int()
        direction = self.get_int()
        title = self.get_string()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['direction', direction])
        self.debug.append(['title', title])


def init(data):
    return AddPainting(data)


def info():
    return {'pid': 153}