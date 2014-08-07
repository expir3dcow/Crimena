from crimena.network.protocol.packet import Packet


class Disconnect(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        self.debug.append(['Disconnected', True])


def init(data):
    return Disconnect(data)


def info():
    return {'pid': 21}