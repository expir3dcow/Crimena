from crimena.network.protocol.packet import Packet

info = {'pid': 21}


class Disconnect(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        self.put_byte(self.pid())

    def decode(self):
        pass


def init(data):
    return Disconnect(data)