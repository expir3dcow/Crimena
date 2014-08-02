import struct
import time
import binascii


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
                print('> R: bytes: {:>3}'.format(len(data)))
                if 1 <= pid <= 8:
                    print('raknet: {!s:>18}'.format(binascii.hexlify(data[:40])))
                    self.handle_raknet(data, addr)
                elif pid == 132:
                    print('mcpe: {!s:>18}'.format(binascii.hexlify(data[:40])))
                    self.handle_mcpe(data, addr)
                else:
                    print('yay new pid {}'.format(pid))  # TODO: check for more

                queue.task_done()
            else:
                time.sleep(.1)  # todo: make it better

    def handle_raknet(self, data, addr):
        reply = None
        pid = data[0]

        packet_in = self.network.packets['raknet'].get(pid, None)
        if packet_in:
            pkt_in = getattr(packet_in['module'], packet_in['name'])(self.server)
            pkt_in.buffer = data
            pkt_in.decode()
            reply = pkt_in.reply()

        if reply:
            for pid in reply:
                packet_out = self.network.packets['raknet'].get(pid, None)
                if packet_out:
                    pkt_out = getattr(packet_out['module'], packet_out['name'])(self.server)
                    dupes = list(set(dir(pkt_in)) & set(dir(pkt_out)))
                    if 'client_port' in dir(pkt_out):
                        pkt_out.__dict__['client_port'] = addr[1]
                    for i in dupes:
                        if not i.startswith('put') and not i.startswith('get') and not i.startswith('__') and not i.startswith('encode') and not i.startswith('decode') and not i.startswith('buffer') and not i.startswith('pid') and not i.startswith('reply') :
                            pkt_out.__dict__[i] = pkt_in.__dict__[i]
                    pkt_out.encode()
                    self.network.send_raknet(pkt_out.buffer, addr)

    def handle_mcpe(self, data, addr):
        pid = data[0]
        cnt = struct.unpack('i',data[1:4]+b'\x00')[0]
        print(cnt)

        pid = data[4]
        print(pid, data[5:])
        # TODO: the rest D: