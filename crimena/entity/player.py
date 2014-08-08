from queue import Queue
import binascii

from crimena.entity.entity import Entity, get_server


# TODO: save player
# TODO: load player


class Player(Entity):
    def __init__(self, addr, client_id, entity_id, mtu_size):
        """Initialize a Player

        :param addr: player address
        :param client_id: client id
        :param entity_id: entity id
        :param mtu_size: mtu size
        """
        Entity.__init__(self, entity_id)
        self.addr = addr
        self.client_id = client_id
        self.mtu_size = mtu_size
        self.server = get_server()
        self.send_queue = Queue()
        self.packet_counter = {'send_ack': 0}  # TODO: resend nack and remove ack
        self.loggedin = False

        self.username = None


    def handle_packet(self, packets, pid, data):
        print('In Player -> pid: %d %s' % (pid, hex(pid)))
        print('Data: %s' % binascii.hexlify(data))

        if pid == 130:
            packet_in = packets['mcpe'].get(int(pid), False)
            if packet_in:
                pkt_in = packet_in['mod'].init(self.server)
                pkt_in.buffer = data
                pkt_in.decode()

                print(pkt_in.username)

                packet_out = packets['mcpe'].get(131, False)
                if packet_out:
                    pkt_out = packet_out['mod'].init(self.server)
                    pkt_out.status = 0
                    pkt_out.encode()
                    self.send_queue.put(pkt_out.buffer)

                packet_out = packets['mcpe'].get(135, False)
                if packet_out:
                    pkt_out = packet_out['mod'].init(self.server)
                    pkt_out.seed = 0
                    pkt_out.generator = 0
                    pkt_out.gamemode = 0
                    pkt_out.entity_id = 0
                    pkt_out.spawnx = 0
                    pkt_out.spawny = 0
                    pkt_out.spawnz = 0
                    pkt_out.x = 0
                    pkt_out.y = 0
                    pkt_out.z = 0
                    pkt_out.encode()
                    self.send_queue.put(pkt_out.buffer)