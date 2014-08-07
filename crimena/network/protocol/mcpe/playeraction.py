from crimena.network.protocol.packet import Packet

info = {'pid': 164}


class PlayerAction(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.action = None
        self.x = None
        self.y = None
        self.z = None
        self.face = None
        self.entity_id = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.action)
        self.put_int(self.x)
        self.put_int(self.y)
        self.put_int(self.z)
        self.put_int(self.face)
        self.put_int(self.entity_id)


    def decode(self):
        self.action = self.get_int()
        self.x = self.get_int()
        self.y = self.get_int()
        self.z = self.get_int()
        self.face = self.get_int()


def init(data):
    return PlayerAction(data)