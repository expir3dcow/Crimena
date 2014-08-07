from crimena.network.protocol.packet import Packet

info = {'pid': 175}


class DropItem(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.unknown = None
        self.item_id = None
        self.item_cnt = None
        self.item_meta = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_byte(self.unknown)
        self.put_short(self.item_id)
        self.put_byte(self.item_cnt)
        self.put_short(self.item_meta)

    def decode(self):
        self.entity_id = self.get_int()
        self.unknown = self.get_byte()
        self.item_id = self.get_short()
        self.item_cnt = self.get_byte()
        self.item_meta = self.get_short()


def init(data):
    return DropItem(data)