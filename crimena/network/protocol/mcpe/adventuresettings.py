from crimena.network.protocol.packet import Packet

info = {'pid': 183}


class AdventureSettings(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.flags = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.flags)

    def decode(self):
        self.flags = self.get_int()


def init(data):
    return AdventureSettings(data)