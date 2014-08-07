from crimena.network.protocol.packet import Packet

info = {'pid': 135}


class StartGame(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.seed = None
        self.generator = None
        self.gamemode = None
        self.entity_id = None
        self.spawnx = None
        self.spawny = None
        self.spawnz = None
        self.x = None
        self.y = None
        self.z = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put_int(self.seed)
        self.put_int(self.generator)
        self.put_int(self.gamemode)
        self.put_int(self.entity_id)
        self.put_int(self.spawnx)
        self.put_int(self.spawny)
        self.put_int(self.spawnz)
        self.put_float(self.x)
        self.put_float(self.y)
        self.put_float(self.z)

    def decode(self):
        self.seed = self.get_int()
        self.generator = self.get_int()
        self.gamemode = self.get_int()
        self.entity_id = self.get_int()
        self.spawnx = self.get_int()
        self.spawny = self.get_int()
        self.spawnz = self.get_int()
        self.x = self.get_float()
        self.y = self.get_float()
        self.z = self.get_float()


def init(data):
    return StartGame(data)