from binascii import unhexlify

def hexFromInt(number):
    hexadecimal = "{0:x}".format(number)
    if len(hexadecimal) % 2 == 1:
        hexadecimal = "0" + hexadecimal
    return hexadecimal

def intFromHex(hexadecimal):
    return int(hexadecimal, 16)

def byteStringFromHex(hexadecimal):
    return unhexlify(hexadecimal)

def bitsFromHex(hexadecimal):
    return format(intFromHex(hexadecimal), 'b').zfill(4 * len(hexadecimal))