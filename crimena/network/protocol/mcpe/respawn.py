from crimena.network.protocol.packet import Packet

info = {'pid': 173}


class Respawn(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_float(self.x)
        self.put_float(self.y)
        self.put_float(self.z)

    def decode(self):
        self.entity_id = self.get_int()
        self.x = self.get_float()
        self.y = self.get_float()
        self.z = self.get_float()


def init(data):
    return Respawn(data)