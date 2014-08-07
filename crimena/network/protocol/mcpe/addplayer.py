from crimena.network.protocol.packet import Packet

info = {'pid': 137}


class AddPlayer(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.client_id = None
        self.username = None
        self.entity_id = None
        self.x = None
        self.y = None
        self.z = None
        self.yaw = None
        self.pitch = None
        self.unknown1 = None
        self.unknown2 = None
        self.metadata = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_long(self.client_id)
        self.put_string(self.username)
        self.put_int(self.entity_id)
        self.put_float(self.x)
        self.put_float(self.y)
        self.put_float(self.z)
        self.put_byte(self.yaw)
        self.put_byte(self.pitch)
        self.put_short(self.unknown1)
        self.put_short(self.unknown2)
        self.put_metadata(self.metadata)  # TODO: make it work

    def decode(self):
        self.client_id = self.get_long()
        self.username = self.get_string()
        self.entity_id = self.get_int()
        self.x = self.get_float()
        self.y = self.get_float()
        self.z = self.get_float()
        self.yaw = self.get_byte()
        self.pitch = self.get_byte()
        self.unknown1 = self.get_short()
        self.unknown2 = self.get_short()
        self.metadata = self.get_metadata()


def init(data):
    return AddPlayer(data)