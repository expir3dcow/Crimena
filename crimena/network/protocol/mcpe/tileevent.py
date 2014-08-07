from crimena.network.protocol.packet import Packet

info = {'pid': 156}


class TileEvent(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.x = None
        self.y = None
        self.z = None
        self.case1 = None
        self.case2 = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.x)
        self.put_int(self.y)
        self.put_int(self.z)
        self.put_int(self.case1)
        self.put_int(self.case2)

    def decode(self):
        self.x = self.get_int()
        self.y = self.get_int()
        self.z = self.get_int()
        self.case1 = self.get_int()
        self.case2 = self.get_int()


def init(data):
    return TileEvent(data)