from crimena.network.protocol.packet import Packet


class Pong(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        time1 = self.get_long()
        time2 = self.get_long()

        self.debug.append(['time1', time1])
        self.debug.append(['time2', time2])


def init(data):
    return Pong(data)


def info():
    return {'pid': 3}