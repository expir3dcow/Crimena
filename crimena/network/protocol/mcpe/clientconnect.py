from crimena.network.protocol.packet import Packet


class ClientConnect(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        client_id = self.get_long()
        session1 = self.get_long()
        session2 = self.get_byte()

        self.debug.append(['client_id', str(client_id)])
        self.debug.append(['session1', session1])
        self.debug.append(['session2', session2])


def init(data):
    return ClientConnect(data)


def info():
    return {'pid': 9}
