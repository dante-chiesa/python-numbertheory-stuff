#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361
import euclid
from baseconvert import baseconvert


def modexp(base, exp, modulo):
    """
    Calculates the modulo exponent, i.e. base ^ exp (mod m)
    """
    # little endian, so [2^0, 2^1, 2^2, ...]
    expbits = baseconvert(exp, 2)

    # partial exponentiation
    partial = base
    result = 1
    for bit in expbits:
        if bit == 1:
            result = (result * partial) % modulo
        partial = (partial ** 2) % modulo
    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("Usage: modexp.py base exp modulo")
    else:
        base = int(sys.argv[1])
        exp = int(sys.argv[2])
        mod = int(sys.argv[3])
        print(str(modexp(base, exp, mod)))
