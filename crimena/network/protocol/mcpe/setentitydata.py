from crimena.network.protocol.packet import Packet


class SetEntityData(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        metadata = self.get_metadata()

        self.debug.append(['entity_id', entity_id])
        # self.debug.append(['metadata', metadata])  # FIXME: make it work


def init(data):
    return SetEntityData(data)


def info():
    return {'pid': 167}