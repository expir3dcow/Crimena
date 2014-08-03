import logging
import os
import time
import struct
from crimena.config.properties import Properties
from crimena.network.network import Network
from crimena.utils.logger import setup_logger

log = logging.getLogger('Crimena')


class Server(object):
    """Main Server class"""

    def __init__(self):
        setup_logger()
        log.debug('Starting Crimena')

        self.server_config = Properties('server.conf')
        self.server_network = Network(self)
        self.server_start_time = time.time() * 1000
        self.server_id = struct.unpack("!Q", os.urandom(8))[0]

        self.isrunning = True

    def start(self):
        self.server_config.load()

        self.server_network.start()

        self.gameloop()

    def gameloop(self):
        while self.isrunning:
            time.sleep(10)

    def get_time_since_start(self):
        return int(time.time()*1000 - self.server_start_time)