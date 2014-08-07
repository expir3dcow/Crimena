from nose.tools import assert_equals
from crimena.utils import binutils as tools


def test_short():
    assert_equals(tools.get_short(b'\x00\x02'), 2)
    assert_equals(tools.put_short(2), b'\x00\x02')


def test_long():
    assert_equals(tools.get_long(b'\x00\x00\x00\x00\x00\x00\x03\xf3'), 1011)
    assert_equals(tools.put_long(4378), b'\x00\x00\x00\x00\x00\x00\x11\x1a')


def test_string():
    s = b'\x00\x06\x49\x6E\x74\x79\x72\x65'
    length = int(tools.get_short(s[:2]))
    assert_equals(length, 6)
    assert_equals(tools.get_string(s[2:length+2]), 'Intyre')
    assert_equals(tools.put_string('Intyre'), s)


def test_triad():
    assert_equals(tools.get_triad(b'\x00\x00\x00'), 0)
    assert_equals(tools.get_triad(b'\x00\x04\xd2'), 1234)
    assert_equals(tools.get_triad(b'\x2e\x16\x00', False), 5678)

    assert_equals(tools.put_triad(1234), b'\x00\x04\xd2')
    assert_equals(tools.put_triad(5678, False), b'\x2e\x16\x00')


def test_int():
    assert_equals(tools.get_int(b'\x00\x00\x00\x00'), 0)
    assert_equals(tools.get_int(b'\x00\x00\x00\x01'), 1)
    assert_equals(tools.put_int(362), b'\x00\x00\x01\x6a')


def test_float():
    assert_equals(tools.get_float(b'\x3f\x80\x00\x00'), 1.0)
    assert_equals(tools.put_float(3.14), b'\x40\x48\xf5\xc3')