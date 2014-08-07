from crimena.network.protocol.packet import Packet

info = {'pid': 160}


class PlayerEquipment(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.item = None
        self.meta = None
        self.slot = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_short(self.item)
        self.put_short(self.meta)
        self.put_byte(self.slot)

    def decode(self):
        self.entity_id = self.get_int()
        self.item = self.get_short()
        self.meta = self.get_short()
        self.slot = self.get_byte()


def init(data):
    return PlayerEquipment(data)