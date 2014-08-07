from crimena.network.protocol.packet import Packet

info = {'pid': 184}


class EntityData(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.x = None
        self.y = None
        self.z = None
        self.namedtag = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.x)
        self.put_byte(self.y)
        self.put_int(self.z)
        self.put(self.namedtag)

    def decode(self):
        self.x = self.get_int()
        self.y = self.get_byte()
        self.z = self.get_int()
        self.namedtag = self.get()  # TODO: check this


def init(data):
    return EntityData(data)