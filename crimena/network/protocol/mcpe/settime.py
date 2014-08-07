from crimena.network.protocol.packet import Packet


class SetTime(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        time = self.get_int()
        self.debug.append(['time', time])
        if len(self.data) > 0:
            started = self.get_byte()
            self.debug.append(['started', started])


def init(data):
    return SetTime(data)


def info():
    return {'pid': 134}