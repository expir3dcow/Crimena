from crimena.network.protocol.packet import Packet


class ContainerSetData(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        window_id = self.get_byte()
        prop = self.get_short()
        value = self.get_short()

        self.debug.append(['window_id', window_id])
        self.debug.append(['property', prop])
        self.debug.append(['value', value])


def init(data):
    return ContainerSetData(data)


def info():
    return {'pid': 179}