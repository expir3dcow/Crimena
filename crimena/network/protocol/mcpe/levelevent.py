from crimena.network.protocol.packet import Packet

info = {'pid': 155}


class LevelEvent(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.event_id = None
        self.x = None
        self.y = None
        self.z = None
        self.data = None

    def encode(self):
        self.put_byte(self.pid())

        self.put_short(self.event_id)
        self.put_int(self.x)
        self.put_short(self.y)
        self.put_int(self.x)
        self.put_int(self.data)

    def decode(self):
        self.event_id = self.get_short()
        self.x = self.get_int()
        self.y = self.get_short()
        self.z = self.get_int()
        self.data = self.get_int()


def init(data):
    return LevelEvent(data)