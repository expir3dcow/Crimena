from crimena.network.protocol.packet import Packet

info = {'pid': 140}


class AddEntity(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.entity_type = None
        self.x = None
        self.y = None
        self.z = None
        self.did = None
        self.speed = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_byte(self.entity_type)
        self.put_float(self.x)
        self.put_float(self.y)
        self.put_float(self.z)
        self.put_int(self.did)
        if self.did > 0:
            self.put_short(self.speed[0])
            self.put_short(self.speed[1])
            self.put_short(self.speed[2])

    def decode(self):
        self.entity_id = self.get_int()
        self.entity_type = self.get_byte()
        self.x = self.get_float()
        self.y = self.get_float()
        self.z = self.get_float()
        self.did = self.get_int()
        if self.did > 0:
            self.speed.append(self.get_short())
            self.speed.append(self.get_short())
            self.speed.append(self.get_short())


def init(data):
    return AddEntity(data)