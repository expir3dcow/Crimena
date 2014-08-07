from crimena.network.protocol.packet import Packet


class MovePlayer(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        x = self.get_float()
        y = self.get_float()
        z = self.get_float()
        yaw = self.get_float()
        pitch = self.get_float()
        body_yaw = self.get_float()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['yaw', yaw])
        self.debug.append(['pitch', pitch])
        self.debug.append(['body_yaw', body_yaw])


def init(data):
    return MovePlayer(data)


def info():
    return {'pid': 149}