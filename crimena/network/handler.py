import logging
import re
import time
import binascii

from crimena.utils import binutils

log = logging.getLogger('debug')
re_pktinfo = re.compile('^[^#].+:', )


class Handler(object):
    def __init__(self, network, server, queue):
        self.network = network
        self.server = server
        self.queue = queue

        while True:
            if not queue.empty():
                data, addr = queue.get()

                # handle the data
                pid = data[0]
                if 1 <= pid <= 8:
                    log.debug('> R: size: {:>4} raknet: {!s}'.format(len(data), binascii.hexlify(data[:40])))
                    self.raknet_handler(data, addr)
                elif pid == 132:
                    log.debug('> R: size: {:>4}   mcpe: {!s}'.format(len(data), binascii.hexlify(data[:40])))
                    self.mcpe_handler(data, addr)
                else:
                    log.debug('yay new pid {}'.format(pid))  # NOTE: check for more

                queue.task_done()
            else:
                time.sleep(.1)  # TODO: make it better

    def raknet_handler(self, data, addr):
        pid = data[0]

        packet_in = self.network.packets['raknet'].get(int(pid), None)
        if packet_in:
            pkt_in = packet_in['mod'].init(self.server)
            pkt_in.buffer = data
            pkt_in.decode()

        if packet_in['info']['reply']:
            self.raknet_reply(pkt_in, packet_in['info'], addr)

    def raknet_reply(self, pkt_in, info, addr):
        for pid in info['reply']:
            packet_out = self.network.packets['raknet'].get(int(pid), None)
            if packet_out:
                pkt_out = packet_out['mod'].init(self.server)
                dupes = list(set(info['fields']) & set(packet_out['info']['fields']))

                for i in dupes:
                    g = getattr(pkt_in, i)
                    setattr(pkt_out, i, g)

                if packet_out['info']['pid'] == 8:
                    setattr(pkt_out, 'client_port', addr[1])

                pkt_out.encode()
                self.network.send_raknet(pkt_out.buffer, addr)

    def mcpe_handler(self, data, addr):
        pid = data[0]
        cnt = binutils.get_triad(data[1:4], False)

        pid = data[4]
        log.debug('%d', pid)
        # TODO: the rest D: