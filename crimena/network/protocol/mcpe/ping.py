from crimena.network.protocol.packet import Packet


class Ping(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        time = self.get_long()

        self.debug.append(['time', time])


def init(data):
    return Ping(data)


def info():
    return {'pid': 0}