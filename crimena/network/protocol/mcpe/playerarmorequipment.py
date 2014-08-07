from crimena.network.protocol.packet import Packet


class PlayerArmorEquipment(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        slot1 = self.get_byte()
        slot2 = self.get_byte()
        slot3 = self.get_byte()
        slot4 = self.get_byte()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['slot1', slot1])
        self.debug.append(['slot2', slot2])
        self.debug.append(['slot3', slot3])
        self.debug.append(['slot4', slot4])


def init(data):
    return PlayerArmorEquipment(data)


def info():
    return {'pid': 161}