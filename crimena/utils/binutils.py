from struct import unpack, pack

# byte
def get_byte(a):
    return unpack('>B', a)[0]

def put_byte(a):
    return pack('>B', a)

# short
def get_short(a):
    return unpack('>H', a)[0]

def put_short(a):
    return pack('>H', a)

# triad
def get_triad(a, big=True):
    if big:
        return unpack('>i', b'\x00' + a)[0]
    else:
        return unpack('<i', a + b'\x00')[0]

def put_triad(a, big=True):
    if big:
        return pack('>i', a)[1:]
    else:
        return pack('<i', a)[:3]

# int
def get_int(a):
    return unpack('>i', a)[0]

def put_int(a):
    return pack('>i', a)

# float
def get_float(a):
    return unpack('>f', a)[0]

def put_float(a):
    return pack('>f', a)

# long
def get_long(a):
    return unpack('>Q', a)[0]

def put_long(a):
    return pack('>Q', a)

# string
def get_string(a):
    return a.decode('utf-8')

def put_string(a):
    r = put_short(len(a)) + a.encode()
    return r