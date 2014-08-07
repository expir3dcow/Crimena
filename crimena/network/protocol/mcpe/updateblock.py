from crimena.network.protocol.packet import Packet

info = {'pid': 152}


class UpdateBlock(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.x)
        self.put_int(self.z)
        self.put_byte(self.y)
        self.put_byte(self.block)
        self.put_byte(self.meta)

    def decode(self):
        self.x = self.get_int()
        self.z = self.get_int()
        self.y = self.get_byte()
        self.block = self.get_byte()
        self.meta = self.get_byte()


def init(data):
    return UpdateBlock(data)