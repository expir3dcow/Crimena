from crimena.network.protocol.packet import Packet


class ClientHandshake(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        security = self.get_byte()
        cookie = self.get_int()
        client_port = self.get_short()
        data_array = self.get(self.get_byte())
        for i in range(0, 9):
            self.get(3)
            self.get(4)
        timestamp = self.get_short()
        session2 = self.get_long()
        session1 = self.get_long()

        self.debug.append(['security', security])
        self.debug.append(['cookie', cookie])
        self.debug.append(['client_port', client_port])
        # self.debug.append(['data_array', data_array])  # FIXME: make it work
        self.debug.append(['timestamp', timestamp])
        self.debug.append(['session2', session2])
        self.debug.append(['session1', session1])


def init(data):
    return ClientHandshake(data)


def info():
    return {'pid': 19}