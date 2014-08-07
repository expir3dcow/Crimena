from crimena.network.protocol.packet import Packet

info = {'pid': 166}
class HurtArmor(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.health = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.health)

    def decode(self):
        self.health = self.get_byte()


def init(data):
    return HurtArmor(data)