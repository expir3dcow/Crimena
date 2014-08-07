import logging
from crimena.entity.player import Player

log = logging.getLogger('crimena')


class EntityHandler(object):
    def __init__(self, server):
        self.server = server
        self.clients = {}
        self.entity_id = 0

    def get_entity_id(self):
        self.entity_id += 1
        return self.entity_id

    def add_player(self, addr, client_id, mtu_size):
        if addr not in self.clients:
            self.clients[addr] = Player(addr, client_id, self.get_entity_id(), mtu_size)
            log.info('Player added')
        else:
            log.info('Player already added')

    def get_player(self, addr):
        if addr in self.clients:
            return self.clients[addr]
        return False