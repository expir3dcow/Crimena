import crimena
from crimena.entity.entity import Entity, get_server


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
        self.packet_counter = {'ack': [], 'nack': []}  # TODO: resend nack and remove ack