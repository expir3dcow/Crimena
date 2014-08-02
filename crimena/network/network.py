from queue import Queue
import socket
import threading
from crimena.network.handler import Handler


class Network(threading.Thread):
    """Network handler"""

    def __init__(self, server):
        super(Network, self).__init__()
        self.daemon = True
        self.server = server
        self.server_ip = '0.0.0.0'
        self.server_port = self.server.server_config.get('port', 19132)

        self.data_in = Queue()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.server_ip, self.server_port))

    def run(self):
        t = threading.Thread(target=Handler, args=([self, self.server, self.data_in, ]))
        t.daemon = True
        t.start()

        while True:
            data, addr = self.sock.recvfrom(2048)
            self.data_in.put([data, addr])

    def send_data(self, buffer, addr):
        self.sock.sendto(buffer, addr)

    def stop(self):
        print('Stopping Network socket')
        self.sock.close()