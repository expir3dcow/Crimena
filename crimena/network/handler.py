import logging
import re
import threading
import time
import binascii

from crimena.network.protocol.mcpepacket import decapsulate
from crimena.utils import binutils


log = logging.getLogger('debug')
re_pktinfo = re.compile('^[^#].+:', )


class Handler(threading.Thread):
    def __init__(self, network, server, queue):
        super(Handler, self).__init__()
        self.daemon = True
        self.name = "Command Handler"

        self.network = network
        self.server = server
        self.queue = queue

    def run(self):
        while self.network.isrunning:
            if not self.queue.empty():
                data, addr = self.queue.get()

                # handle the data
                pid = data[0]
                if 1 <= pid <= 8:
                    # log.debug('> R: size: {:>4} raknet: {!s}'.format(len(data), binascii.hexlify(data[:40])))
                    self.raknet_handler(data, addr)
                elif pid == 132:
                    # log.debug('> R: size: {:>4}   mcpe: {!s}'.format(len(data), binascii.hexlify(data[:40])))
                    player = self.mcpe_handler(data, addr)
                    if player and not player.send_queue.empty():
                        print('need to send data!')
                        self.mcpe_sender(player)
                elif pid == 192 or pid == 160:
                    print('ACK Received')  # TODO: fix me :D
                elif pid == 0:  # ping
                    print('Ping Received!')
                else:
                    log.debug('yay new pid {}\n--> {!s}'.format(pid, binascii.hexlify(data)))  # NOTE: check for more

                self.queue.task_done()
            else:
                time.sleep(.1)  # TODO: make it better
        log.debug('Packet Handler thread stopped')

    def raknet_handler(self, data, addr):
        pid = data[0]

        packet_in = self.network.packets['raknet'].get(int(pid), False)
        if packet_in:
            pkt_in = packet_in['mod'].init(self.server)
            pkt_in.buffer = data
            pkt_in.decode()

            if packet_in['info'].get('reply', False):
                self.raknet_reply(pkt_in, packet_in['info'], addr)

    def raknet_reply(self, pkt_in, info, addr):
        for pid in info['reply']:
            packet_out = self.network.packets['raknet'].get(int(pid), False)
            if packet_out:
                pkt_out = packet_out['mod'].init(self.server)
                dupes = list(set(info['fields']) & set(packet_out['info']['fields']))

                for i in dupes:
                    g = getattr(pkt_in, i)
                    setattr(pkt_out, i, g)

                if pid == 8:
                    setattr(pkt_out, 'client_port', addr[1])
                    self.server.server_entities.add_player(addr, pkt_in.client_id, pkt_in.mtu_size)

                pkt_out.encode()
                self.network.send_raknet(pkt_out.buffer, addr)

    def mcpe_handler(self, full_data, addr):
        player = self.server.server_entities.get_player(addr)
        if not player:
            return

        packets = decapsulate(full_data)  # unpack data packet
        self.send_ack(addr, packets['packet_count'])  # send ACK

        for data in packets['packets']:
            # while len(data) > 0:
            log.debug('\tdata: %s', binascii.hexlify(data))
            pid = data[0]
            # print('New Packet ID %s' % hex(pid))
            data = data[1:]

            pkt_in = None
            pkt_out = None
            if pid == 0:
                pkt_in = self.network.packets['mcpe'][pid]['mod'].init(self.server)
                pkt_in.buffer = data
                pkt_in.decode()

                pkt_out = self.network.packets['mcpe'][3]['mod'].init(self.server)
                pkt_out.time1 = pkt_in.time
                pkt_out.time2 = 1  # TODO: make it work
                pkt_out.encode()
            elif pid == 9:
                pkt_in = self.network.packets['mcpe'][pid]['mod'].init(self.server)
                pkt_in.buffer = data
                pkt_in.decode()

                pkt_out = self.network.packets['mcpe'][16]['mod'].init(self.server)
                pkt_out.cookie_security = b'\x04\x3f\x57\xff\xf4'  # hard-coded!
                pkt_out.port = player.addr[1]
                pkt_out.session1 = pkt_in.session1
                pkt_out.session2 = 1  # TODO: fix it
                pkt_out.encode()
            elif pid == 19:
                pkt_in = self.network.packets['mcpe'][pid]['mod'].init(self.server)
                pkt_in.buffer = data
                pkt_in.decode()
            elif pid == 130:
                data = player.handle_packet(self.network.packets, pid, data)
            else:
                print('TODO: %d %s' % (pid, hex(pid)))  # TODO: for missing packets
                data = b''

            if pkt_in and len(pkt_in.buffer) > 0:
                data = pkt_in.buffer
                print('there is more data')
            else:
                data = b''

            if pkt_out:  # TODO: add to player send queue
                print('\tpacket added to queue')
                player.send_queue.put(pkt_out.buffer)
            return player
        return False

    def mcpe_sender(self, player):
        buffer = bytearray(b'\x84')

        while player.send_queue.qsize() > 0:
            data = player.send_queue.get()
            # TODO: check mtu
            # TODO: make packet
            buffer.extend(binutils.put_triad(player.packet_counter['send_ack'], False))
            player.packet_counter['send_ack'] += 1
            buffer.extend(b'\x00')
            buffer.extend(binutils.put_short(len(data)*8))
            buffer.extend(data)
        self.network.send_raknet(buffer, player.addr)

    def send_ack(self, addr, start, end=False):
        packet_out = self.network.packets['mcpe'].get(192, False)
        if packet_out:
            pkt_out = packet_out['mod'].init(self.server)
            pkt_out.unknown = 1
            pkt_out.single = 1 if not end else 0
            pkt_out.start = start
            pkt_out.end = end
            pkt_out.encode()
            self.network.send_raknet(pkt_out.buffer, addr)

