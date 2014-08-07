from crimena.network.protocol.packet import Packet

info = {'pid': 182}


class Chat(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.message = None

    def encode(self):
        self.put_byte(self.pid())

        self.put_string(self.message)

    def decode(self):
        self.message = self.get_string()


def init(data):
    return Chat(data)