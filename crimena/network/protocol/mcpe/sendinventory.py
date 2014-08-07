from crimena.network.protocol.packet import Packet

info = {'pid': 174}


class SendInventory(Packet):
    def __init__(self, data):
        Packet.__init__(self, data)
        self.entity_id = None
        self.window_id = None
        self.items = []
        self.armor = []

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.entity_id)
        self.put_byte(self.window_id)
        self.put_short(len(self.items))
        for item in self.items:
            self.put_short(item[0])
            self.put_byte(item[1])
            self.put_short(item[2])
        if self.window_id == 1:
            for armor in self.armor:
                self.put_short(armor[0])
                self.put_byte(armor[1])
                self.put_short(armor[2])


    def decode(self):
        self.entity_id = self.get_int()
        self.window_id = self.get_byte()
        count = self.get_short()
        for i in range(0, count):  # TODO: item class?
            item_id = self.get_short()
            item_cnt = self.get_byte()
            item_meta = self.get_short()
            self.items.append([item_id, item_cnt, item_meta])
        if self.window_id == 1:
            for i in range(0, 4):  # TODO: armor class?
                armor_id = self.get_short()
                armor_cnt = self.get_byte()
                armor_meta = self.get_short()
                self.armor.append(armor_id, armor_cnt, armor_meta)


def init(data):
    return SendInventory(data)