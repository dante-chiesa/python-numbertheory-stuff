# Created by Dante Chiesa for Professor B________, Math 361

from trialdivision import trialdivision
from modexp import modexp
from typing import List, Union, Tuple, cast, Any, NamedTuple

#  strong fermat composite test


class StrongFermatResult(NamedTuple):
    bs: List[int]

    def __str__(self) -> str:
        lines = []
        for x in range(len(self.bs)):
            lines.append(f"b{x}:\t{self.bs[x]}")
        return "\n".join(lines)


def strongfermat_raw(n: int, base: int) -> bool:

    div_result = trialdivision(n - 1, [2])

    power_of_two: int = div_result.factors[0].exp

    oddpart: int
    if len(div_result.factors) > 1:
        oddpart = div_result.factors[1].prime
    elif div_result.remaining is not None:
        oddpart = div_result.remaining
    else:
        oddpart = 1

    bs: List[int] = []
    cur_val = modexp(base, oddpart, n)
    if cur_val == n - 1:
        cur_val = -1
    bs.append(cur_val)

    for _ in range(power_of_two - 1):
        cur_val = modexp(cur_val, 2, n)
        if cur_val == n - 1:
            cur_val = -1
        bs.append(cur_val)

    return StrongFermatResult(bs)


def strongfermat(n: int, base: int) -> bool:
    """
    Performs the strong fermat test to see if a number is definitely
    composite or probably prime
    n : number to test
    base : number to test with
    
    false -> definitely composite
    true -> n is pseudoprime relative to base
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False  # even numbers are always composite

    div_result = trialdivision(n - 1, [2])

    power_of_two: int = div_result.factors[0].exp

    oddpart: int
    if len(div_result.factors) > 1:
        oddpart = div_result.factors[1].prime
    elif div_result.remaining is not None:
        oddpart = div_result.remaining
    else:
        oddpart = 1

    cur_val = modexp(base, oddpart, n)
    # only check for +1 on the first try
    if cur_val == 1 or cur_val == n - 1:
        return True  # n is pseudoprime

    for _ in range(power_of_two - 1):
        cur_val = modexp(cur_val, 2, n)
        if cur_val == n - 1:  # equal to -1 mod n
            return True

    return False
