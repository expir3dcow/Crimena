from crimena.network.protocol.packet import Packet


class ACK(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        unknown = self.get_short()
        single = self.get_byte()
        start = self.get_triad()

        self.debug.append(['Unknown', unknown])
        self.debug.append(['Single', single])
        self.debug.append(['Start', start])

        if single == 0:
            end = self.get_triad()
            self.debug.append(['End', end])


def init(data):
    return ACK(data)


def info():
    return {'pid': 192}