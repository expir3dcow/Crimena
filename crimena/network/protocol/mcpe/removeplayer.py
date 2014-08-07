from crimena.network.protocol.packet import Packet


class RemovePlayer(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        client_id = self.get_long()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['client_id', client_id])


def init(data):
    return RemovePlayer(data)


def info():
    return {'pid': 138}