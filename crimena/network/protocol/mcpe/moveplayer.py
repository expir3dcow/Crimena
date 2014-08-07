from crimena.network.protocol.packet import Packet

info = {'pid': 149}


class MovePlayer(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.x = None
        self.y = None
        self.z = None
        self.yaw = None
        self.pitch = None
        self.body_yaw = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_float(self.x)
        self.put_float(self.y)
        self.put_float(self.z)
        self.put_float(self.yaw)
        self.put_float(self.pitch)
        self.put_float(self.body_yaw)

    def decode(self):
        self.entity_id = self.get_int()
        self.x = self.get_float()
        self.y = self.get_float()
        self.z = self.get_float()
        self.yaw = self.get_float()
        self.pitch = self.get_float()
        self.body_yaw = self.get_float()


def init(data):
    return MovePlayer(data)