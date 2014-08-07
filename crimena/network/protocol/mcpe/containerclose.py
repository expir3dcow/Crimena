from crimena.network.protocol.packet import Packet

info = {'pid': 177}


class ContainerClose(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.window_id = None

    def encode(self):
        self.put_byte(self.pid())

        self.put_byte(self.window_id)

    def decode(self):
        self.window_id = self.get_byte()


def init(data):
    return ContainerClose(data)