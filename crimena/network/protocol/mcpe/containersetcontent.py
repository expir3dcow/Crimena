from crimena.network.protocol.packet import Packet

info = {'pid': 180}


class ContainerSetContent(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.window_id = None
        self.slots = []
        self.hotbar = []

    def encode(self):
        self.put_byte(info['pid'])

        self.put_byte(self.window_id)
        self.put_short(len(self.slots))
        for slot in self.slots:
            self.put_short(slot[0])
            self.put_byte(slot[2])
            self.put_short(slot[1])
        if self.window_id == 0:
            for slot in self.hotbar:
                self.put_int(slot)

    def decode(self):
        self.window_id = self.get_byte()
        count = self.get_short()
        for i in range(0, count):  # TODO: get_slot? :)
            item_id = self.get_short()
            item_cnt = self.get_byte()
            item_meta = self.get_short()
            self.slots.append([item_id, item_meta, item_cnt])
        if self.window_id == 0:
            count = self.get_short()
            for i in range(0, count):
                self.hotbar.append(self.get_int())


def init(data):
    return ContainerSetContent(data)