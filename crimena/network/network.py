import logging
from queue import Queue
import socket
import threading
import binascii
import time

from crimena.network.handler import Handler
from crimena.utils.packetloader import load_packets


log = logging.getLogger('debug')


class Network(threading.Thread):
    """Network handler"""

    def __init__(self, server):
        super(Network, self).__init__()
        self.daemon = True
        self.name = "Network"

        self.packets = {}
        self.data_in = Queue()

        self.server = server
        self.server_ip = '0.0.0.0'
        self.server_port = self.server.server_config.get('port', 19132)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.server_ip, self.server_port))
        self.sock.settimeout(1)
        self.isrunning = True

    def run(self):
        self.packets = load_packets()
        log.debug('Loaded {} raknet and {} mcpe packets'.format(len(self.packets['raknet']), len(self.packets['mcpe'])))

        handler = Handler(self, self.server, self.data_in)
        handler.start()

        while self.isrunning:
            try:
                data, addr = self.sock.recvfrom(2048)
                self.data_in.put([data, addr])
            except socket.timeout:
                pass

        print('Stopping %s' % self.name)
        self.sock.close()

    def send_raknet(self, buffer, addr):
        log.debug('< S: size: {:>4} {!s:>8}'.format(len(buffer), binascii.hexlify(buffer[:40])))
        self.sock.sendto(buffer, addr)

    def stop(self):
        log.info('Stopping Network socket')
        self.isrunning = False
        time.sleep(1)