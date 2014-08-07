from crimena.network.protocol.packet import Packet

info = {'pid': 151}


class RemoveBlock(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.x = None
        self.z = None
        self.y = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_int(self.x)
        self.put_int(self.z)
        self.put_byte(self.y)

    def decode(self):
        self.entity_id = self.get_int()
        self.x = self.get_int()
        self.z = self.get_int()
        self.y = self.get_byte()


def init(data):
    return RemoveBlock(data)