from crimena.network.protocol.packet import Packet

info = {'pid': 192}


class ACK(Packet):
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
        self.put_triad(self.start)
        if self.end:
            self.put_triad(self.end)

    def decode(self):
        self.unknown = self.get_short()
        self.single = self.get_byte()
        self.start = self.get_triad()

        if self.single == 0:
            self.end = self.get_triad()


def init(data):
    return ACK(data)