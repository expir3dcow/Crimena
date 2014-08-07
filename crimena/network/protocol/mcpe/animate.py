from crimena.network.protocol.packet import Packet

info = {'pid': 172}


class Animate(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.action = None
        self.entity_id = None

    def encode(self):
        self.put_byte(self.pid())

        self.put_byte(self.action)
        self.put_int(self.entity_id)

    def decode(self):
        self.action = self.get_byte()
        self.entity_id = self.get_int()


def init(data):
    return Animate(data)