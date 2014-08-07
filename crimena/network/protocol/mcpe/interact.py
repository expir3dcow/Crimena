from crimena.network.protocol.packet import Packet

info = {'pid': 162}


class Interact(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.action = None
        self.entity_id = None
        self.target_id = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.action)
        self.put_int(self.entity_id)
        self.put_int(self.target_id)

    def decode(self):
        self.action = self.get_byte()
        self.entity_id = self.get_int()
        self.target_id = self.get_int()

def init(data):
    return Interact(data)