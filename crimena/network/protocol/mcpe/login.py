from crimena.network.protocol.packet import Packet

info = {'pid': 130}


class Login(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.username = None
        self.protocol1 = None
        self.protocol2 = None
        self.client_id = None
        self.login_data = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_string(self.username)
        self.put_int(self.protocol1)
        self.put_int(self.protocol2)
        self.put_int(self.client_id)
        self.put_string(self.login_data)

    def decode(self):
        self.username = self.get_string()
        self.protocol1 = self.get_int()
        self.protocol2 = self.get_int()
        self.client_id = self.get_int()
        self.login_data = self.get_string()


def init(data):
    return Login(data)