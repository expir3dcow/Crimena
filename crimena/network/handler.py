import time
import binascii
from crimena.network.protocol.raknet.raknet01 import RakNet01
from crimena.network.protocol.raknet.raknet05 import RakNet05
from crimena.network.protocol.raknet.raknet06 import RakNet06
from crimena.network.protocol.raknet.raknet1c import RakNet1c


class Handler(object):

    def __init__(self, network, server, queue):
        self.network = network
        self.server = server
        self.queue = queue

        while True:
            if not queue.empty():
                data, addr = queue.get()
                print('R: \tbytes: {}\ndata: \t{!s}'.format(len(data), binascii.hexlify(data)))
                # handle the data
                self.handle_data(data, addr)

                queue.task_done()
            else:
                time.sleep(.05) # todo: make it better xD

    def handle_data(self, data, addr):
        pid = data[0]
        if pid == 1:
            # get data from client packet
            pkt_in = RakNet01()
            pkt_in.buffer = data
            pkt_in.decode()

            # make packet to send
            pkt_out = RakNet1c()
            pkt_out.ping_id = self.server.get_time_since_start()
            pkt_out.server_id = 0
            pkt_out.magic = pkt_in.magic
            pkt_out.identifier = 'MCCPP;Demo;Hello World'
            pkt_out.encode()
            self.network.send_data(pkt_out.buffer, addr)

        elif pid == 5:
            # get data from client packet
            pkt_in = RakNet05()
            pkt_in.buffer = data
            pkt_in.decode()

            # make packet to send
            pkt_out = RakNet06()
            pkt_out.magic = pkt_in.magic
            pkt_out.server_id = self.server.server_id
            pkt_out.mtu_size = pkt_in.mtu_size
            pkt_out.encode()
            self.network.send_data(pkt_out.buffer, addr)