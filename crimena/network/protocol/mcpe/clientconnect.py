from crimena.network.protocol.packet import Packet

info = {'pid': 9}


class ClientConnect(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.client_id = None
        self.session1 = None
        self.session2 = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_long(self.client_id)
        self.put_long(self.session1)
        self.put_byte(self.session2)

    def decode(self):
        self.client_id = self.get_long()
        self.session1 = self.get_long()
        self.session2 = self.get_byte()


def init(data):
    return ClientConnect(data)
