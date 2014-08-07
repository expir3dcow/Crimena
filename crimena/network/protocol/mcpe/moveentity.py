from crimena.network.protocol.packet import Packet

info = {'pid': 144}


class MoveEntity(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.entities = []

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(len(self.entities))
        for entity in self.entities:
            self.put_int(entity[0])
            self.put_float(entity[1])
            self.put_float(entity[2])
            self.put_float(entity[3])
            self.put_float(entity[4])
            self.put_float(entity[5])

    def decode(self):
        entity_count = self.get_int()
        for i in range(0, entity_count):
            entity_id = self.get_int()
            entity_x = self.get_float()
            entity_y = self.get_float()
            entity_z = self.get_float()
            entity_yaw = self.get_float()
            entity_pitch = self.get_float()
            self.entities.append(entity_id, entity_x, entity_y, entity_z, entity_yaw, entity_pitch)


def init(data):
    return MoveEntity(data)