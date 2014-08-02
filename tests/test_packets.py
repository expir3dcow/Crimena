import nose.tools as tools
from crimena.network.protocol.raknet.raknet01 import RakNet01


def test_raknet01_decode():
    ping_id = 3789965
    magic = b'\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78'

    pkt = RakNet01()
    pkt.buffer = b'\x01\x00\x00\x00\x00\x00\x39\xd4\x8d\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78'
    pkt.decode()
    tools.assert_equals(pkt.ping_id, ping_id)
    tools.assert_equals(pkt.magic, magic)