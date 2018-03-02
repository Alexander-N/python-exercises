# An alternative solution emphasizing EAFP instead of LBYL
# (see https://docs.python.org/glossary.html#term-eafp)
# With no checks performed on the input, this solution is rather fast -
# though still much slower, of course, then the built-in int(s, base=16).

hexdigits_to_int = dict(zip('0123456789', range(10)))
hexdigits_to_int.update(zip('abcdef', range(10, 16)))
hexdigits_to_int.update(zip('ABCDEFG', range(10, 16)))


def hexa(s):
    result = 0
    c = None
    try:
        for c in s:
            result = result*16 + hexdigits_to_int[c]
    except KeyError:
        c = None
    if c is None:
        # s was empty or triggered KeyError
        raise ValueError('Invalid hexadecimal string')
    return result
