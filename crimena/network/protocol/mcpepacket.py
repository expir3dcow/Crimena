import struct


class Mcpepacket(object):

    def __init__(self, data):
        self.data = data
        self.pid = self.data[0]
        self.count = struct.unpack('>i', data[1:4] + b'\x00')[0]
        self.data = self.data[4:]

    def unpack(self):
        # TODO: make it work
        while self.data:
            encid = self.data[0]
            print(encid)

            length = int(struct.unpack('>H', self.data[1:3])[0]/8.)
            print(length)

            if encid == 64:
                count = struct.unpack('>i', self.data[3:6] + b'\x00')[0]
                self.data = self.data[6:]
            else:
                print('Add me {}'.format(encid))

            print(len(self.data), self.data)
            self.data = b''