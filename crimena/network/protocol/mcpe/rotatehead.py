from crimena.network.protocol.packet import Packet

info = {'pid': 148}


class RotateHead(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.entities = []

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(len(self.entities))
        for entity in self.entities:
            self.put_int(entity[0])
            self.put_byte(entity[1])


    def decode(self):
        entity_count = self.get_int()
        for i in range(0, entity_count):
            entity_id = self.get_int()
            entity_rotation = self.get_byte()
            self.entities.append([entity_id, entity_rotation])


def init(data):
    return RotateHead(data)