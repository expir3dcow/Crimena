from crimena.network.protocol.packet import Packet


class Interact(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        action = self.get_byte()
        entity_id = self.get_int()
        target = self.get_int()

        self.debug.append(['action', action])
        self.debug.append(['entity_id', entity_id])
        self.debug.append(['target', target])


def init(data):
    return Interact(data)


def info():
    return {'pid': 162}