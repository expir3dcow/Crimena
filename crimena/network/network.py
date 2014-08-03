import inspect
import logging
import os
from queue import Queue
import re
import socket
import threading
import importlib.abc

from crimena.network.handler import Handler


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
        self.packets = self.load_packets()
        log.debug('Loaded {} raknet and {} mcpe packets'.format(len(self.packets['raknet']), len(self.packets['mcpe'])))

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
        log.info('Stopping Network socket')
        self.sock.close()

    def load_packets(self):
        packets = {'raknet': {}, 'mcpe': {}}
        packet_info = ['name', 'pid', 'reply']
        importlib.import_module('.protocol', package='crimena.network')

        pysearchre = re.compile('^[^_].*\.py$',)
        for packet in packets:
            importlib.import_module('.'+packet, package='crimena.network.protocol')

            pluginfiles = filter(pysearchre.search,
                                 os.listdir(os.path.join(os.path.dirname(__file__),
                                                         'protocol', packet)))
            form_module = lambda fp: '.' + os.path.splitext(fp)[0]
            plugins = map(form_module, pluginfiles)

            for p in plugins:
                mod = importlib.import_module(p, package=''.join("crimena.network.protocol." + packet))
                info = {'obj': mod.init(self.server)}

                doc_splitted = inspect.getdoc(mod).split('\n')
                for line in doc_splitted:
                    if not line.startswith("#"):
                        line = line.split('=')
                        if len(line) > 1 and line[0] in packet_info:
                            if line[0] == 'reply':
                                info[line[0]] = info.get(line[0], line[1].split(','))
                            elif line[1].isdigit():
                                info[line[0]] = info.get(line[0], int(line[1]))
                            else:
                                info[line[0]] = info.get(line[0], line[1])
                # log.debug('%s[%s] <- %s', packet, info['pid'], info)
                packets[packet][info['pid']] = info
        return packets