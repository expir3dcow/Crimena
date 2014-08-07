from crimena.network.protocol.packet import Packet


class MoveEntity(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_count = self.get_int()
        # print 'Entity count:', entity_count
        for i in range(0, entity_count):
            entity_id = self.get_int()
            entity_x = self.get_float()
            entity_y = self.get_float()
            entity_z = self.get_float()
            entity_yaw = self.get_float()
            entity_pitch = self.get_float()
        self.debug.append(['entity_count', entity_count])


def init(data):
    return MoveEntity(data)


def info():
    return {'pid': 144}