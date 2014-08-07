from crimena.network.protocol.packet import Packet


class ContainerSetContent(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        window_id = self.get_byte()
        count = self.get_short()
        for i in range(0, count):
            id = self.get_short()
            cnt = self.get_byte()
            damage = self.get_short()
        if window_id == 0:
            count = self.get_short()
            for i in range(0, count):
                hotbar = self.get_int()

        self.debug.append(['window_id', window_id])
        self.debug.append(['count', count])


def init(data):
    return ContainerSetContent(data)


def info():
    return {'pid': 180}