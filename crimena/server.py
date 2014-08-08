import logging
import os
import time
import struct

from crimena.config.properties import Properties
from crimena.entity.handler import EntityHandler
from crimena.network.network import Network
from crimena.utils.logger import setup_logger
from crimena.utils.singleton import Singleton


log = logging.getLogger('Crimena')


class Server(metaclass=Singleton):
    """Main Server class"""

    def __init__(self):
        setup_logger()
        log.debug('Starting Crimena')

        self.server_config = Properties('server.conf')
        self.server_network = Network(self)
        self.server_start_time = time.time() * 1000
        self.server_id = struct.unpack("!Q", os.urandom(8))[0]
        self.server_entities = EntityHandler(self)

        self.isrunning = True

    def start(self):
        self.server_config.load()

        self.server_network.start()

        self.gameloop()

    def stop(self):
        print('TODO: save and kick players')
        print('TODO: stop network listener')
        self.server_network.stop()

        print('TODO: save world')
        print('TODO: save config files')
        self.isrunning = False
        pass

    def gameloop(self):
        while self.isrunning:
            time.sleep(10)  # TODO: xD

    def get_time_since_start(self):
        return int(time.time()*1000 - self.server_start_time)