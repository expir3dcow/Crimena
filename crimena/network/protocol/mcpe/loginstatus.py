from crimena.network.protocol.packet import Packet

info = {'pid': 131}


class LoginStatus(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.status = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.status)

    def decode(self):
        self.status = self.get_int()


def init(data):
    return LoginStatus(data)