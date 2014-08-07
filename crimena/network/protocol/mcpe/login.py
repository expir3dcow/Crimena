from crimena.network.protocol.packet import Packet


class Login(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        username = self.get_string()
        protocol1 = self.get_int()
        protocol2 = self.get_int()
        client_id = self.get_int()
        login_data = self.get_string()

        self.debug.append(['username', username])
        self.debug.append(['protocol1', str(protocol1)])
        self.debug.append(['protocol2', str(protocol2)])
        self.debug.append(['client_id', str(client_id)])
        self.debug.append(['login_data', login_data])


def init(data):
    return Login(data)


def info():
    return {'pid': 130}