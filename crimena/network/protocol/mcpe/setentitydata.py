from crimena.network.protocol.packet import Packet

info = {'pid': 167}


class SetEntityData(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.metadata = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_metadata(self.metadata)

    def decode(self):
        self.entity_id = self.get_int()
        self.metadata = self.get_metadata()


def init(data):
    return SetEntityData(data)