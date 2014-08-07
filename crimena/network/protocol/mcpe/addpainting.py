from crimena.network.protocol.packet import Packet

info = {'pid': 153}


class AddPainting(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.x = None
        self.y = None
        self.z = None
        self.direction = None
        self.title = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_int(self.x)
        self.put_int(self.y)
        self.put_int(self.z)
        self.put_int(self.direction)
        self.put_string(self.title)

    def decode(self):
        self.entity_id = self.get_int()
        self.x = self.get_int()
        self.y = self.get_int()
        self.z = self.get_int()
        self.direction = self.get_int()
        self.title = self.get_string()


def init(data):
    return AddPainting(data)