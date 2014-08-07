from crimena.network.protocol.packet import Packet


class StartGame(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        seed = self.get_int()
        generator = self.get_int()
        gamemode = self.get_int()
        eid = self.get_int()
        spawnx = self.get_int()
        spawny = self.get_int()
        spawnz = self.get_int()
        x = self.get_float()
        y = self.get_float()
        z = self.get_float()

        self.debug.append(['seed', seed])
        self.debug.append(['generator', generator])
        self.debug.append(['gamemode', gamemode])
        self.debug.append(['eid', eid])
        self.debug.append(['spawnX', spawnx])
        self.debug.append(['spawnY', spawny])
        self.debug.append(['spawnZ', spawnz])
        self.debug.append(['x', x])
        self.debug.append(['y', y])
        self.debug.append(['z', z])


def init(data):
    return StartGame(data)


def info():
    return {'pid': 135}