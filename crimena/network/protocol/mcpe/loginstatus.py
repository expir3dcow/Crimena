from crimena.network.protocol.packet import Packet


class LoginStatus(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        status = self.get_int()

        self.debug.append(['status', status])


def init(data):
    return LoginStatus(data)


def info():
    return {'pid': 131}