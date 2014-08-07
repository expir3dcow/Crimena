from crimena.network.protocol.packet import Packet

info =  {'pid': 163}


class UseItem(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.x = None
        self.y = None
        self.z = None
        self.face = None
        self.item = None
        self.meta = None
        self.entity_id = None
        self.fx = None
        self.fy = None
        self.fz = None
        self.posx = None
        self.posy = None
        self.posz = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.x)
        self.put_int(self.y)
        self.put_int(self.z)
        self.put_int(self.face)
        self.put_short(self.item)
        self.put_short(self.meta)
        self.put_int(self.entity_id)
        self.put_float(self.fx)
        self.put_float(self.fy)
        self.put_float(self.fz)
        self.put_float(self.posx)
        self.put_float(self.posy)
        self.put_float(self.posz)

    def decode(self):
        self.x = self.get_int()
        self.y = self.get_int()
        self.z = self.get_int()
        self.face = self.get_int()
        self.item = self.get_short()
        self.meta = self.get_short()
        self.entity_id = self.get_int()
        self.fx = self.get_float()
        self.fy = self.get_float()
        self.fz = self.get_float()
        self.posx = self.get_float()
        self.posy = self.get_float()
        self.posz = self.get_float()


def init(data):
    return UseItem(data)