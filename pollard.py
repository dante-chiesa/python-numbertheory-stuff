# Created by Dante Chiesa for Professor B________, Math 361

from typing import NamedTuple, List, Callable
from modexp import modexp
import euclid


class RhoResultLine(NamedTuple):
    step: int
    x: int
    y: int
    gcd: int


class RhoResult(NamedTuple):
    divisor: int
    table: List[RhoResultLine]

    def __repr__(self):
        return "RhoResult(\n" + "\n".join((repr(x) for x in self.table)) + "\n)"


def rhomethod_raw(
    N: int, fun: Callable[[int], int], x_0: int = 2, *, max_iter: int = 10000
):
    """
    Calculates a divisor of a number by Pollard's Rho Method
    """
    results = []
    x: int = x_0
    y: int = fun(fun(x_0) % N) % N
    stepnum: int = 1
    success: bool = False
    for _ in range(max_iter):
        gcd: int = euclid.gcd(y - x, N)
        results.append(RhoResultLine(stepnum, x, y, gcd))
        if gcd != 1 and gcd != N:
            success = True
            break
        x = fun(x) % N
        y = fun(fun(y) % N) % N
        stepnum += 1

    divisor = None
    if success:
        divisor = results[-1].gcd
    return RhoResult(divisor, results)


def rhomethod(
    N: int, fun: Callable[[int], int], x_0: int = 2, *, max_iter: int = 10000
):

    """
    Calculates a divisor of a number by Pollard's Rho Method
    May return None if nothing was found in max_iter iterations
    """
    return rhomethod_raw(N, fun, x_0, max_iter=max_iter).divisor


class PMinusOneLine(NamedTuple):
    step: int
    exp: str
    val: int  # represents a^exp! - 1 (mod N)
    gcd: int


class PMinusOneResult(NamedTuple):
    divisor: int
    table: List[PMinusOneLine]

    def __repr__(self):
        return "PMinusOneResulT(\n" + "\n".join((repr(x) for x in self.table)) + "\n)"


def pminusonemethod_raw(N: int, x_0: int = 2, *, max_iter: int = 10000):
    """
    Attempts to find a prime factor by Pollard's P - 1 Method
    """
    results = []

    step: int = 1
    val: int = x_0

    success: bool = False

    for _ in range(max_iter):
        if val != 1:
            gcd: int = euclid.gcd(val - 1, N)
        else:
            gcd: int = 0  # special handling to avoid divide by 0
        expstr = f"{step}!"
        results.append(PMinusOneLine(step, expstr, val - 1, gcd))
        if gcd != 1 and gcd != N:
            success = True
            break
        if val == 0:
            success = False
            break
        step += 1
        val = modexp(val, step, N)

    divisor = None
    if success:
        divisor = results[-1].gcd
    return PMinusOneResult(divisor, results)


def pminusonemethod(N: int, x_0: int = 2, *, max_iter: int = 10000):
    return pminusonemethod_raw(N, x_0, max_iter=max_iter).divisor
