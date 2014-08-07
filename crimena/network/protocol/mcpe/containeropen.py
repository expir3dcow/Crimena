from crimena.network.protocol.packet import Packet


class ContainerOpen(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        window_id = self.get_byte()
        container_type = self.get_byte()
        slots = self.get_short()
        x = self.get_int()
        y = self.get_int()
        z = self.get_int()

        self.debug.append(['window_id', window_id])
        self.debug.append(['container_type', container_type])
        self.debug.append(['slots', slots])
        self.debug.append(['x', x])
        self.debug.append(['z', z])


def init(data):
    return ContainerOpen(data)


def info():
    return {'pid': 176}