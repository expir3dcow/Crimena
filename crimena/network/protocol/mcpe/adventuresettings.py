from crimena.network.protocol.packet import Packet


class AdventureSettings(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        flags = self.get_int()

        self.debug.append(['flags', flags])


def init(data):
    return AdventureSettings(data)


def info():
    return {'pid': 183}