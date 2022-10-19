#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361
import euclid


def multinv(val, modulo):
    """
    finds the multiplicative inverse of `val` mod `modulo`,
    i.e. the number such that val * inverse is equal to 1 (mod modulo)
    """
    table = euclid.euclid(modulo, val)
    gcd = euclid.gcdfromtable(table)
    if gcd != 1:
        return "NaN"
    row = table[-1]
    x0 = ()
    # set x0 to the coefficient of val
    # in the eqn x0*val = y0*modmodulo = 1
    if row[1] == val:
        x0 = row[0]
    else:
        x0 = row[2]
    return x0 % modulo


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: multinv.py value modulo")
    else:
        val = int(sys.argv[1])
        modulo = int(sys.argv[2])
        print(str(multinv(val, modulo)))
