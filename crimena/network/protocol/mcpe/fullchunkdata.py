from crimena.network.protocol.packet import Packet

info = {'pid': 186}


# TODO: make it work
class FullChunkData(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)
        self.packed_chunk = None

    def encode(self):
        self.put_byte(info['pid'])

        self.put(self.packed_chunk)

    def decode(self):
        self.packed_chunk = self.get()


def init(data):
    return FullChunkData(data)
