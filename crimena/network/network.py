import os
from queue import Queue
import re
import socket
import threading
from crimena.network.handler import Handler
import importlib.abc


class Network(threading.Thread):
    """Network handler"""

    def __init__(self, server):
        super(Network, self).__init__()
        self.daemon = True
        self.server = server
        self.server_ip = '0.0.0.0'
        self.server_port = self.server.server_config.get('port', 19132)

        self.packets = self.load_packets()
        print('Loaded {} raknet and {} mcpe packets'.format(len(self.packets['raknet']), len(self.packets['mcpe'])))

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

    def send_raknet(self, buffer, addr):
        # print('< S: \tbytes: {:>3}'.format(len(buffer)))
        # print('raknet: \t{!s:>18}'.format(binascii.hexlify(buffer[:40])))
        self.sock.sendto(buffer, addr)

    def stop(self):
        print('Stopping Network socket')
        self.sock.close()

    def load_packets(self):
        packets = {'raknet': {}, 'mcpe': {}}
        for t in packets:
            pysearchre = re.compile('^[a-z].*.py$', re.IGNORECASE)
            print(os.path.join(os.path.dirname(__file__),
                               'protocol', t))
            pluginfiles = filter(pysearchre.search,
                                 os.listdir(os.path.join(os.path.dirname(__file__),
                                                         'protocol', t)))
            form_module = lambda fp: '.' + os.path.splitext(fp)[0]
            plugins = map(form_module, pluginfiles)

            importlib.import_module('.protocol', package='crimena.network')
            importlib.import_module('.' + t, package='crimena.network.protocol')

            for plugin in plugins:
                if not plugin.startswith('__'):
                    clz_name = plugin.lstrip('.').capitalize()
                    mod = importlib.import_module(plugin, package="crimena.network.protocol." + t)
                    print(clz_name)  # Debug
                    new_clz = getattr(mod, clz_name)(self.server)
                    packets[t][new_clz.pid()] = packets[t].get(new_clz.pid(), {
                        'name': clz_name,
                        'pid': new_clz.pid(),
                        'module': mod,
                    })
        return packets