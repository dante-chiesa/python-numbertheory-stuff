#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361
import euclid
from phi import phi
from trialdivision import trialdivision, TrialDivResult, Factor
from modexp import modexp
from typing import List, Tuple, Any


def _gen_divisors_from_factorization_helper(factlist: List[Factor]) -> List[int]:

    if len(factlist) == 0:
        return [1]

    (prime, exp) = factlist[-1]

    # recurse
    divisors: List[int] = _gen_divisors_from_factorization_helper(factlist[:-1])
    newdivisors: List[int] = []
    for i in range(1, exp + 1):
        newdivisors.extend((x * (prime ** i) for x in divisors))
    divisors.extend(newdivisors)
    return divisors


def _gen_divisors_from_factorization(div_res: TrialDivResult) -> List[int]:
    factors = div_res.factors
    if div_res.remaining is not None:
        factors.append(Factor(div_res.remaining, 1))  # assume remaining is prime
    divisors = _gen_divisors_from_factorization_helper(factors)
    divisors.sort()
    return divisors


def _ordbruteforce(x: int, n: int) -> int:
    gcd = euclid.gcd(x, n)
    if gcd != 1:
        raise Exception("order is undefined, gcd is not 1")
    phi_n = phi(n)
    factors = trialdivision(phi_n)
    divisors = _gen_divisors_from_factorization(factors)
    for exp in divisors:
        if modexp(x, exp, n) == 1:
            return exp
    # phi_n is the default, but it should have already been calculated in the
    # divisors above, so if we get here something went wrong
    raise Exception("something went wrong, ord could not be factored")


def order(x: int, n: int) -> int:
    """
    Calculates the order of x mod n, i.e. the lowest positive integer m such that
    x ^ m === 1 (modn)
    Undefined if gcd(x,n) is not 1
    """
    return _ordbruteforce(x, n)


def _prettyprint(x: int, n: int) -> None:
    ord = order(x, n)
    print(f"The order of {x} mod {n} is {ord}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: order.py x n to calculate the order of x mod n")
    else:
        _prettyprint(int(sys.argv[1]), int(sys.argv[2]))
