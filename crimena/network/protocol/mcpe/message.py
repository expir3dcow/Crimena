from crimena.network.protocol.packet import Packet


class Message(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        source = self.get_string()
        message = self.get_string()

        self.debug.append(['source', source])
        self.debug.append(['message', message])


def init(data):
    return Message(data)


def info():
    return {'pid': 133}