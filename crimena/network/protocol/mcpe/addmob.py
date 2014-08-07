from crimena.network.protocol.packet import Packet

info = {'pid': 136}


class AddMob(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.entity_type = None
        self.x = None
        self.y = None
        self.z = None
        self.yaw = None
        self.pitch = None
        self.metadata = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_int(self.entity_type)
        self.put_float(self.x)
        self.put_float(self.y)
        self.put_float(self.z)
        self.put_byte(self.yaw)
        self.put_metadata(self.metadata)  # TODO: make it work

    def decode(self):
        self.entity_id = self.get_int()
        self.entity_type = self.get_int()
        self.x = self.get_float()
        self.y = self.get_float()
        self.z = self.get_float()
        self.yaw = self.get_byte()
        self.pitch = self.get_byte()
        self.metadata = self.get_metadata()


def init(data):
    return AddMob(data)