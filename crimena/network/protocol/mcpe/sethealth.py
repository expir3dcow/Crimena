from crimena.network.protocol.packet import Packet

info = {'pid': 170}


class SetHealth(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.health = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.health)

    def decode(self):
        self.health = self.get_byte()


def init(data):
    return SetHealth(data)