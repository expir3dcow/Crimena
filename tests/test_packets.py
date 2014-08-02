from nose.tools import *

from crimena.network.protocol.raknet.raknet01 import Raknet01
from crimena.network.protocol.raknet.raknet05 import Raknet05
from crimena.network.protocol.raknet.raknet06 import Raknet06
from crimena.network.protocol.raknet.raknet07 import Raknet07
from crimena.network.protocol.raknet.raknet08 import Raknet08
from crimena.network.protocol.raknet.raknet1c import Raknet1c

magic = b'\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78'


class Server(object):
    server_id = 0

    def __init__(self):
        pass

    def get_time_since_start(self):
        return 4


def test_raknet01():
    pkt = Raknet01(None)
    pkt.buffer = b'\x01\x00\x00\x00\x00\x02\x92\xde\xe3\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78'
    pkt.decode()
    assert_equals(pkt.magic, magic)
    assert_equals(pkt.ping_id, 43179747)


def test_raknet05():
    pkt = Raknet05(None)
    pkt.buffer = b'\x05\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78\x05'+b'\x00'*1464
    pkt.decode()
    assert_equals(pkt.magic, magic)
    assert_equals(pkt.protocol_version, 5)
    assert_equals(pkt.mtu_size, 1464)


def test_raknet06():
    pkt = Raknet06(Server)
    pkt.magic = magic
    pkt.mtu_size = 1446
    assert_equals(pkt.buffer, bytearray(b''))
    pkt.encode()
    assert_not_equal(pkt.buffer, bytearray(b''))
    assert_equals(len(pkt.buffer), 28)


def test_raknet07():
    pkt = Raknet07(None)
    pkt.buffer = b'\x07\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78\x04\x3f\x57\xff\xf4\x4a\xbc' \
                 b'\x05\xa6\xff\xff\xff\xff\xab\x06\x69\x95'
    pkt.decode()
    assert_equals(pkt.magic, magic)
    assert_equals(pkt.security, 4)
    assert_equals(pkt.cookie, b'\x3f\x57\xff\xf4')
    assert_equals(pkt.server_port, 19132)
    assert_equals(pkt.mtu_size, 1446)
    assert_equals(pkt.client_id, 18446744072283908501)


def test_raknet08():
    pkt = Raknet08(Server)
    pkt.client_port = 34832
    pkt.mtu_size = 1446
    pkt.magic = magic
    assert_equals(pkt.buffer, bytearray(b''))
    pkt.encode()
    assert_not_equal(pkt.buffer, bytearray(b''))
    assert_equals(len(pkt.buffer), 30)


def test_raknet1c():
    pkt = Raknet1c(Server())
    pkt.ping_id = 4
    pkt.magic = magic
    assert_equals(pkt.buffer, bytearray(b''))
    pkt.encode()
    assert_not_equal(pkt.buffer, bytearray(b''))
    assert_equals(len(pkt.buffer), 53)