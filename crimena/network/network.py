import logging
from queue import Queue
import socket
import threading
import binascii

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

    def run(self):
        self.packets = load_packets()
        log.debug('Loaded {} raknet and {} mcpe packets'.format(len(self.packets['raknet']), len(self.packets['mcpe'])))

        t = threading.Thread(target=Handler, args=([self, self.server, self.data_in, ]))
        t.daemon = True
        t.start()

        while True:
            data, addr = self.sock.recvfrom(2048)
            self.data_in.put([data, addr])

    def send_raknet(self, buffer, addr):
        log.debug('< S: size: {:>4} raknet: {!s:>8}'.format(len(buffer), binascii.hexlify(buffer[:40])))
        self.sock.sendto(buffer, addr)

    def stop(self):
        log.info('Stopping Network socket')
        self.sock.close()