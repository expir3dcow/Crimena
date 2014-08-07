from crimena.network.protocol.packet import Packet

info = {'pid': 138}


class RemovePlayer(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.client_id = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_long(self.client_id)

    def decode(self):
        self.entity_id = self.get_int()
        self.client_id = self.get_long()


def init(data):
    return RemovePlayer(data)