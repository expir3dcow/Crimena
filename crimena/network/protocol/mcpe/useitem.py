from crimena.network.protocol.packet import Packet


class UseItem(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        x = self.get_int()
        y = self.get_int()
        z = self.get_int()
        face = self.get_int()
        item = self.get_short()
        meta = self.get_short()
        entity_id = self.get_int()
        fx = self.get_float()
        fy = self.get_float()
        fz = self.get_float()
        posx = self.get_float()
        posy = self.get_float()
        posz = self.get_float()

        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['face', face])
        self.debug.append(['item', item])
        self.debug.append(['meta', meta])
        self.debug.append(['entity_id', entity_id])
        self.debug.append(['fx', fx])
        self.debug.append(['fy', fy])
        self.debug.append(['fz', fz])
        self.debug.append(['posx', posx])
        self.debug.append(['posy', posy])
        self.debug.append(['posz', posz])


def init(data):
    return UseItem(data)


def info():
    return {'pid': 163}