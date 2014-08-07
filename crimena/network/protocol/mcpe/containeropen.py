from crimena.network.protocol.packet import Packet

info = {'pid': 176}


class ContainerOpen(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.window_id = None
        self.container_type = None
        self.slots = None
        self.x = None
        self.y = None
        self.z = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.window_id)
        self.put_byte(self.container_type)
        self.put_short(self.slots)
        self.put_int(self.x)
        self.put_int(self.y)
        self.put_int(self.z)

    def decode(self):
        self.window_id = self.get_byte()
        self.container_type = self.get_byte()
        self.slots = self.get_short()
        self.x = self.get_int()
        self.y = self.get_int()
        self.z = self.get_int()


def init(data):
    return ContainerOpen(data)