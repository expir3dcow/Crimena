from crimena.network.protocol.packet import Packet


class ContainerClose(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        window_id = self.get_byte()

        self.debug.append(['window_id', window_id])


def init(data):
    return ContainerClose(data)


def info():
    return {'pid': 177}