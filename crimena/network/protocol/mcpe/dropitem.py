from crimena.network.protocol.packet import Packet


class DropItem(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        unknown = self.get_byte()
        item_id = self.get_short()
        item_cnt = self.get_byte()
        item_meta = self.get_short()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['unknown', unknown])
        self.debug.append(['item_id', item_id])
        self.debug.append(['item_cnt', item_cnt])
        self.debug.append(['item_meta', item_meta])


def init(data):
    return DropItem(data)


def info():
    return {'pid': 175}