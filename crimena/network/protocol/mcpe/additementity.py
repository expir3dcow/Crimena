from crimena.network.protocol.packet import Packet

info = {'pid': 142}


class AddItemEntity(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.slot_id = None
        self.slot_cnt = None
        self.slot_meta = None
        self.x = None
        self.y = None
        self.z = None
        self.yaw = None
        self.pitch = None
        self.roll = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.entity_id)
        self.put_short(self.slot_id)
        self.put_byte(self.slot_cnt)
        self.put_short(self.slot_meta)
        self.put_float(self.x)
        self.put_float(self.y)
        self.put_float(self.z)
        self.put_byte(self.yaw)
        self.put_byte(self.pitch)
        self.put_byte(self.roll)

    def decode(self):
        self.entity_id = self.get_int()
        self.slot_id = self.get_short()
        self.slot_cnt = self.get_byte()
        self.slot_meta = self.get_short()
        self.x = self.get_float()
        self.y = self.get_float()
        self.z = self.get_float()
        self.yaw = self.get_byte()
        self.pitch = self.get_byte()
        self.roll = self.get_byte()


def init(data):
    return AddItemEntity(data)