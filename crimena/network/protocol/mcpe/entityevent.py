from crimena.network.protocol.packet import Packet

info = {'pid': 157}


class EntityEvent(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.event = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_byte(self.event)

    def decode(self):
        self.entity_id = self.get_int()
        self.event = self.get_byte()


def init(data):
    return EntityEvent(data)