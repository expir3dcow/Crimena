import binascii
import logging

from crimena.utils import binutils


log = logging.getLogger('debug')

def decapsulate(data):
    # log.debug(binascii.hexlify(data))

    packet_count = binutils.get_triad(data[1:4], False)  # TODO: return me!
    data = data[4:]

    # decapsulate here. loop until no data
    packets = []
    data_count = []
    while len(data) > 0:
        enc_id = data[0]
        length = binutils.get_short(data[1:3])
        data = data[3:]

        if enc_id == 0:
            pass
        elif enc_id == 64:
            data_count.append(binutils.get_triad(data[0:3]))
            data = data[3:]
        elif enc_id == 96:
            data_count.append(binutils.get_triad(data[0:3]))
            data = data[7:]  # Unknown, just skip it ;)
        else:
            log.debug('Unknown enc_id found')
            log.debug(binascii.hexlify(data))
            data = b''  # TODO: ;)

        packets.append(data[:length])
        data = data[length:]
    return {'packets': packets, 'packet_count': packet_count, 'data_count': data_count}