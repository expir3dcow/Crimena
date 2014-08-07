from crimena.network.protocol.packet import Packet

info = {'pid': 178}


class ContainerSetSlot(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.window_id = None
        self.slot = None
        self.item_id = None
        self.item_cnt = None
        self.item_meta = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.window_id)
        self.put_short(self.slot)
        self.put_short(self.item_id)
        self.put_byte(self.item_cnt)
        self.put_short(self.item_meta)

    def decode(self):
        self.window_id = self.get_byte()
        self.slot = self.get_short()
        self.item_id = self.get_short()
        self.item_cnt = self.get_byte()
        self.item_meta = self.get_byte()


def init(data):
    return ContainerSetSlot(data)