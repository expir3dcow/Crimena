from crimena.network.protocol.packet import Packet


class LevelEvent(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        event_id = self.get_short()
        x = self.get_int()
        y = self.get_short()
        z = self.get_int()
        data = self.get_int()

        self.debug.append(['event_id', event_id])
        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])
        self.debug.append(['data', data])


def init(data):
    return LevelEvent(data)


def info():
    return {'pid': 155}