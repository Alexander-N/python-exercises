_hex_code = dict(zip('0123456789', range(10)))
_hex_code.update(zip('abcdef', range(10, 16)))
_hex_code.update(zip('ABCDEFG', range(10, 16)))


def hexa(s):
    result = 0
    c = None
    try:
        for c in s:
            result = result*16 + _hex_code[c]
    except KeyError:
        c = None
    if c is None:
        # s was empty or triggered KeyError
        raise ValueError('Invalid hexadecimal string')
    return result
