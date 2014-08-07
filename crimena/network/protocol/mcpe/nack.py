from crimena.network.protocol.packet import Packet

info = {'pid': 160}


class NACK(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.unknown = None
        self.single = None
        self.start = None
        self.end = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_short(self.unknown)
        self.put_byte(self.single)
        self.put_triad(self.start, False)

    def decode(self):
        self.unknown = self.get_short()
        self.single = self.get_byte()
        self.start = self.get_triad()

        if self.single == 0:
            self.end = self.get_triad()


def init(data):
    return NACK(data)