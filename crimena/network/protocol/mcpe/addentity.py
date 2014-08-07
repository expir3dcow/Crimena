from crimena.network.protocol.packet import Packet


class AddEntity(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        entity_type = self.get_byte()
        x = self.get_float()
        y = self.get_float()
        z = self.get_float()
        did = self.get_int()
        if did > 0:
            speedx = self.get_short()
            speedy = self.get_short()
            speedz = self.get_short()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['entity_type', entity_type])
        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['did', did])


def init(data):
    return AddEntity(data)


def info():
    return {'pid': 140}