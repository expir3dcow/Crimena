from crimena.network.protocol.packet import Packet


class ContainerSetSlot(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        window_id = self.get_byte()
        slot = self.get_short()
        item_id = self.get_short()
        item_cnt = self.get_byte()
        item_meta = self.get_byte()

        self.debug.append(['window_id', window_id])
        self.debug.append(['slot', slot])
        self.debug.append(['item_id', item_id])
        self.debug.append(['item_cnt', item_cnt])
        self.debug.append(['item_meta', item_meta])


def init(data):
    return ContainerSetSlot(data)


def info():
    return {'pid': 178}