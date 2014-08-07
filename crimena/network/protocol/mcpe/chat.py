from crimena.network.protocol.packet import Packet


class Chat(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        message = self.get_string()

        self.debug.append(['message', message])


def init(data):
    return Chat(data)


def info():
    return {'pid': 182}