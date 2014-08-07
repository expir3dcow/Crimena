from crimena.network.protocol.packet import Packet


class SetEntityMotion(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_count = self.get_int()
        # print 'Entity count:', entity_count
        for i in range(0, entity_count):
            entity_id = self.get_int()
            entity_motx = self.get_short()
            entity_moty = self.get_short()
            entity_motz = self.get_short()

        self.debug.append(['entity_count', entity_count])


def init(data):
    return SetEntityMotion(data)


def info():
    return {'pid': 168}