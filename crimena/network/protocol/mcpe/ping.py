from crimena.network.protocol.packet import Packet

info = {'pid': 0}


class Ping(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.time = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_long(self.time)

    def decode(self):
        time = self.get_long()


def init(data):
    return Ping(data)