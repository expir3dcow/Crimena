import zlib

from crimena.network.protocol.packet import Packet


class FullChunkData(Packet):

    def __init__(self, data):
        Packet.__init__(self, data)

    def encode(self):
        pass

    def decode(self):
        packed_chunk = self.get()

        dc = zlib.decompressobj(zlib.MAX_WBITS)
        self.chunk = dc.decompress(packed_chunk)
        self.debug.append(['packed_chunk size', len(packed_chunk)])


def init(data):
    return FullChunkData(data)


def info():
    return {'pid': 186}
