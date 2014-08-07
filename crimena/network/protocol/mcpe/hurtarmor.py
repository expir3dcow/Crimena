from crimena.network.protocol.packet import Packet


class HurtArmor(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        health = self.get_byte()

        self.debug.append(['health', health])


def init(data):
    return HurtArmor(data)


def info():
    return {'pid': 166}