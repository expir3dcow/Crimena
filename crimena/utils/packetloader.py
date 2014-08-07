import importlib
import os
import re


def load_packets():
    packets = {'raknet': {}, 'mcpe': {}}
    importlib.import_module('.protocol', package='crimena.network')

    pysearchre = re.compile('^[^_].*\.py$',)
    for packet in packets:
        importlib.import_module('.'+packet, package='crimena.network.protocol')

        packet_files = filter(pysearchre.search,
                              os.listdir(os.path.join(os.path.dirname(__file__),
                                                      '../network/protocol', packet)))
        form_module = lambda fp: '.' + os.path.splitext(fp)[0]
        packets_map = map(form_module, packet_files)

        package_name = "crimena.network.protocol." + packet
        for p in packets_map:
            mod = importlib.import_module(p, package=package_name)
            pinfo = mod.info()
            packets[packet][pinfo['pid']] = {'mod': mod, 'info': pinfo}
    return packets