from crimena.network.protocol.packet import Packet


class SendInventory(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        entity_id = self.get_int()
        window_id = self.get_byte()
        count = self.get_short()
        for i in range(0, count):
            id = self.get_short()
            cnt = self.get_byte()
            meta = self.get_short()
        if window_id == 1:
            for i in range(0, 4):
                id = self.get_short()
                cnt = self.get_byte()
                meta = self.get_short()

        self.debug.append(['entity_id', entity_id])
        self.debug.append(['window_id', window_id])
        self.debug.append(['count', count])



def init(data):
    return SendInventory(data)


def info():
    return {'pid': 174}