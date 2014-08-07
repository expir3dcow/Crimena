from crimena.network.protocol.packet import Packet


class PlayerEquipment(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        item = self.get_short()
        meta = self.get_short()
        slot = self.get_byte()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['item', item])
        self.debug.append(['meta', meta])
        self.debug.append(['slot', slot])


def init(data):
    return PlayerEquipment(data)


def info():
    return {'pid': 160}