from crimena.network.protocol.packet import Packet

info = {'pid': 134}


class SetTime(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.time = None
        self.started = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.time)
        if self.started:
            self.put_byte(self.started)

    def decode(self):
        self.time = self.get_int()
        if len(self.data) > 0:
            self.started = self.get_byte()


def init(data):
    return SetTime(data)