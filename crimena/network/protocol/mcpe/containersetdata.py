from crimena.network.protocol.packet import Packet

info = {'pid': 179}


class ContainerSetData(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.window_id = None
        self.prop = None
        self.value = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.window_id)
        self.put_short(self.prop)
        self.put_short(self.value)

    def decode(self):
        self.window_id = self.get_byte()
        self.prop = self.get_short()
        self.value = self.get_short()


def init(data):
    return ContainerSetData(data)