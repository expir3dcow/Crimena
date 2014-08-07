from crimena.network.protocol.packet import Packet

info = {'pid': 161}


class PlayerArmorEquipment(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.slot1 = None
        self.slot2 = None
        self.slot3 = None
        self.slot4 = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_byte(self.slot1)
        self.put_byte(self.slot2)
        self.put_byte(self.slot3)
        self.put_byte(self.slot4)

    def decode(self):
        self.entity_id = self.get_int()
        self.slot1 = self.get_byte()  # player armor class?
        self.slot2 = self.get_byte()
        self.slot3 = self.get_byte()
        self.slot4 = self.get_byte()


def init(data):
    return PlayerArmorEquipment(data)