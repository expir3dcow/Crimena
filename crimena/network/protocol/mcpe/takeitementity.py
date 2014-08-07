from crimena.network.protocol.packet import Packet

info = {'pid': 143}


class TakeItemEntity(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.target_id = None
        self.entity_id = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.target_id)
        self.put_int(self.entity_id)

    def decode(self):
        self.target_id = self.get_int()
        self.entity_id = self.get_int()


def init(data):
    return TakeItemEntity(data)