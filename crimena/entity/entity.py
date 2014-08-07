import crimena.server


class Entity(object):
    def __init__(self, entity_id):
        """

        :param entity_id: entity id
        """
        self.entity_id = entity_id
        pass


def get_server():
    return crimena.server.Server()

