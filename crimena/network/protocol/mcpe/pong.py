from crimena.network.protocol.packet import Packet

info = {'pid': 3}


class Pong(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.time1 = None
        self.time2 = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_long(self.time1)
        self.put_long(self.time2)

    def decode(self):
        self.time1 = self.get_long()
        self.time2 = self.get_long()


def init(data):
    return Pong(data)