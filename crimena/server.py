import os
import time
import struct
from crimena.config.properties import Properties
from crimena.network.network import Network


class Server(object):
    """Main Server class"""

    def __init__(self):
        print('Starting Crimena')
        self.server_config = Properties('server.conf')
        # self.server_world = World()  # todo: make it work
        self.server_network = Network(self)
        self.isrunning = True
        self.server_start_time = time.time()*1000
        self.server_id = struct.unpack("!Q", os.urandom(8))[0]

    def start(self):
        self.server_config.load()

        # self.server_world.load()

        self.server_network.start()

        self.gameloop()

        # self.server_network.stop()
        # self.server_config.save()
        pass

    def gameloop(self):
        # command listener?
        # tps?
        # scheduler?
        # events?
        while self.isrunning:
            time.sleep(10)

    def get_time_since_start(self):
        return int(time.time()*1000 - self.server_start_time)