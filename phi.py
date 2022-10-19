#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361

from trialdivision import trialdivision


def phi(num: int) -> int:
    """
    Computes Euler's Phi function, aka Euler's Totient Function
    The calculation entails prime factorization, so numbers whose greatest
    prime factor isn't in primes.txt (greater than 10,000) are not supported
    """
    divres = trialdivision(num)
    if divres.remaining is not None:
        # number wasn't completely factorable
        raise ArithmeticError(f"{num} is not factorable by trial division")
    primes = [p for (p, _) in divres.factors]
    result = int(num)  # ensure arbitrary-precision int, not float
    for p in primes:
        # integers are arbitrary precision but floats are limited, keep to int
        # by doing N/p instead of N * (1-1/p)
        result = result - result // int(p)
    # result is always an int, but the division converts it to float
    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: phi.py num")
    else:
        print(phi(int(sys.argv[1])))
