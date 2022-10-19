#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361

import math
from typing import List, Any, Tuple, Union, NamedTuple

UNFACTORABLE = "Unfactorable!"


class Factor(NamedTuple):
    prime: int
    exp: int


class TrialDivResult(NamedTuple):
    factors: List[Factor]
    remaining: int = None

    def __str__(self) -> str:
        out = ""
        out = " * ".join((f"{fac.prime}^{fac.exp}" for fac in self.factors))

        if self.remaining is not None:
            extra = f"{self.remaining} (UNFACTORABLE)"
            out = " * ".join([out, extra])
        return out


def _getprimes():
    with open("primes.txt", "r") as f:
        primes = (int(x) for x in f.readlines())
        return primes


def trialdivision(num: int, primes: List[int] = None) -> TrialDivResult:
    """
    performs prime factorization by trial division, using a pre-existing list
    of prime numbers. this may be specified as an argument,
    or if not specified will be read from "primes.txt"
    returns a list of (prime, exponent) pairs.
    the last in the list may be an unfactorable number, raised to
    """
    factors: List[Factor] = []
    if primes is None:
        primes = _getprimes()
    for prime in primes:
        if num == 1:
            break
        if prime * prime > num:
            # n less than p^2, and all numbers less than p are not factors,
            # so n is prime
            factors.append(Factor(num, 1))
            num = 1
            break
        count = 0
        while num % prime == 0:
            num = num // prime
            count += 1
        if count > 0:
            factors.append(Factor(prime, count))
    remaining: int = None
    if num != 1:
        remaining = num
    return TrialDivResult(factors, remaining)


def _factortostring(fac):
    (prime, exp) = fac
    if exp == UNFACTORABLE:
        return "(unfactorable) " + str(prime)
    else:
        return str(prime) + "^" + str(exp)


def prettyprint(factors):
    print(" * ".join((_factortostring(fac) for fac in factors)))


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: trialdivision.py x")
    else:
        num = int(sys.argv[1])
        prettyprint(trialdivision(num))
