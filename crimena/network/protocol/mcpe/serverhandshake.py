from crimena.network.protocol.packet import Packet


class ServerHandshake(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        security = self.get_byte()
        cookie = self.get_int()
        port = self.get_short()
        for i in range(0, 10):
            self.get(3)
            self.get(4)
        security_flag = self.get(1)
        session1 = self.get_long()
        session2 = self.get_long()

        self.debug.append(['security', security])
        self.debug.append(['cookie', cookie])
        self.debug.append(['port', port])
        # self.debug.append(['security_flag', security_flag])  # FIXME: make it work
        self.debug.append(['session1', session1])
        self.debug.append(['session2', session2])


def init(data):
    return ServerHandshake(data)


def info():
    return {'pid': 16}