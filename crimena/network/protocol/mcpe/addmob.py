from crimena.network.protocol.packet import Packet


class AddMob(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        entity_type = self.get_int()
        x = self.get_float()
        y = self.get_float()
        z = self.get_float()
        yaw = self.get_byte()
        pitch = self.get_byte()
        metadata = self.get_metadata()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['entity_type', entity_type])
        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['yaw', yaw])
        self.debug.append(['pitch', pitch])
        # self.debug.append(['metadata', binascii.hexlify(metadata)])  # FIXME: make it work


def init(data):
    return AddMob(data)


def info():
    return {'pid': 136}