from crimena.network.protocol.packet import Packet


class AddItemEntity(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        slot_id = self.get_short()
        slot_cnt = self.get_byte()
        slot_meta = self.get_short()
        x = self.get_float()
        y = self.get_float()
        z = self.get_float()
        yaw = self.get_byte()
        pitch = self.get_byte()
        roll = self.get_byte()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['slot_id', slot_id])
        self.debug.append(['slot_cnt', slot_cnt])
        self.debug.append(['slot_meta', slot_meta])
        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['yaw', yaw])
        self.debug.append(['pitch', pitch])
        self.debug.append(['roll', roll])


def init(data):
    return AddItemEntity(data)


def info():
    return {'pid': 142}