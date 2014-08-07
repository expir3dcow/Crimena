from crimena.network.protocol.packet import Packet

info = {'pid': 168}


class SetEntityMotion(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.entities = []

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(len(self.entities))
        for entity in self.entities:
            self.put_int(entity[0])
            self.put_short(entity[1])
            self.put_short(entity[2])
            self.put_short(entity[3])

    def decode(self):
        entity_count = self.get_int()
        for i in range(0, entity_count):
            entity_id = self.get_int()
            entity_motx = self.get_short()
            entity_moty = self.get_short()
            entity_motz = self.get_short()
            self.entities.append([entity_id, entity_motx, entity_moty, entity_motz])


def init(data):
    return SetEntityMotion(data)