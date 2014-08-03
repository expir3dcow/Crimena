import inspect
import logging
import re
import struct
import time
import binascii

log = logging.getLogger('debug')
repktinfo = re.compile('^[^#].+:',)


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
                    log.debug('> R: size: %s raknet: %s', len(data), binascii.hexlify(data[:40]))
                    self.handle_raknet(data, addr)
                elif pid == 132:
                    log.debug('> R: size: %s mcpe: %s', len(data), binascii.hexlify(data[:40]))
                    self.handle_mcpe(data, addr)
                else:
                    log.debug('yay new pid {}'.format(pid))  # TODO: check for more

                queue.task_done()
            else:
                time.sleep(.1)  # TODO: make it better

    def handle_raknet(self, data, addr):
        reply = None
        pid = data[0]

        packet_in = self.network.packets['raknet'].get(int(pid), None)
        if packet_in:
            pkt_in = packet_in['obj']
            pkt_in.buffer = data
            pkt_in.decode()
            reply = packet_in['reply']

        if reply:
            doc_in = inspect.getdoc(pkt_in).split('\n')
            doc_in_filter = filter(repktinfo.search, doc_in)

            for pid in reply:
                packet_out = self.network.packets['raknet'].get(int(pid), None)
                if packet_out:
                    log.debug('send back: %s', packet_out['name'])
                    pkt_out = packet_out['obj']

                    doc_out = inspect.getdoc(pkt_out).split('\n')
                    doc_out_filter = filter(repktinfo.search, doc_out)

                    dupes = list(set(doc_in_filter) & set(doc_out_filter))
                    for i in dupes:
                        if 'packet_id' not in i and len(i) > 0:
                            atr = i.split(':')[0]
                            g = getattr(pkt_in, atr)
                            setattr(pkt_out, atr, g)

                    if packet_out['pid'] == 8:
                        setattr(pkt_out, 'client_port', addr[1])

                    pkt_out.encode()
                    self.network.send_raknet(pkt_out.buffer, addr)

    def handle_mcpe(self, data, addr):
        pid = data[0]
        cnt = struct.unpack('i',data[1:4]+b'\x00')[0]

        pid = data[4]
        log.debug('%d', pid)
        # TODO: the rest D: