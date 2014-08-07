from crimena.network.protocol.packet import Packet

info = {'pid': 154}
class Explode(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.x = None
        self.y = None
        self.z = None
        self.radius = None
        self.records = []

    def encode(self):
        self.put_byte(info['pid'])

        self.put_float(self.x)
        self.put_float(self.y)
        self.put_float(self.z)
        self.put_float(self.radius)
        self.put_int(len(self.records))
        if len(self.radius) > 0:
            for record in self.records:
                self.put_byte(record[0])
                self.put_byte(record[1])
                self.put_byte(record[2])


    def decode(self):
        self.x = self.get_float()
        self.y = self.get_float()
        self.z = self.get_float()
        self.radius = self.get_float()
        record_cnt = self.get_int()
        self.records = []
        if record_cnt > 0:
            for i in range(0, record_cnt):
                rx = self.get_byte()
                ry = self.get_byte()
                rz = self.get_byte()
                self.records.append([rx, ry, rz])


def init(data):
    return Explode(data)