from crimena.network.protocol.packet import Packet

info = {'pid': 133}


class Message(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.source = None
        self.message = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_string(self.source)
        self.put_string(self.message)

    def decode(self):
        self.source = self.get_string()
        self.message = self.get_string()


def init(data):
    return Message(data)