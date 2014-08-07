from crimena.network.protocol.packet import Packet

info = {'pid': 171}


class SetSpawnPosition(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.x = None
        self.y = None
        self.z = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.x)
        self.put_int(self.z)
        self.put_byte(self.y)

    def decode(self):
        self.x = self.get_int()
        self.z = self.get_int()
        self.y = self.get_byte()


def init(data):
    return SetSpawnPosition(data)