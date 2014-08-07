from crimena.network.protocol.packet import Packet


class AddPlayer(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        client_id = self.get_long()
        username = self.get_string()
        entity_id = self.get_int()
        x = self.get_float()
        y = self.get_float()
        z = self.get_float()
        yaw = self.get_byte()
        pitch = self.get_byte()
        unknown1 = self.get_short()
        unknown2 = self.get_short()
        metadata = self.get_metadata()

        self.debug.append(['client_id', str(client_id)])
        self.debug.append(['username', username])
        self.debug.append(['entity_id', str(entity_id)])
        self.debug.append(['x', str(x)])
        self.debug.append(['y', str(y)])
        self.debug.append(['z', str(z)])
        self.debug.append(['yaw', str(yaw)])
        self.debug.append(['pitch', str(pitch)])
        self.debug.append(['unknown1', str(unknown1)])
        self.debug.append(['unknown2', str(unknown2)])
        # self.debug.append(['metadata', binascii.hexlify(metadata)])  # FIXME: make it work


def init(data):
    return AddPlayer(data)


def info():
    return {'pid': 137}