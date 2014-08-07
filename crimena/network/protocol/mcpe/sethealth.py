from crimena.network.protocol.packet import Packet


class SetHealth(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        health = self.get_byte()

        self.debug.append(['health', health])


def init(data):
    return SetHealth(data)


def info():
    return {'pid': 170}