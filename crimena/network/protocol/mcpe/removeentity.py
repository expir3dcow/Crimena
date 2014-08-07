from crimena.network.protocol.packet import Packet

info = {'pid': 141}


class RemoveEntity(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)

    def decode(self):
        self.entity_id = self.get_int()


def init(data):
    return RemoveEntity(data)