# Created by Dante Chiesa for Professor B________, Math 361

from strongfermat import strongfermat
import random
from typing import Generator

_random_seeded = False


def _randiter(max: int) -> Generator[int, None, None]:
    """
    Yields an infinite sequence of random integers from the set [0, max)
    """
    global _random_seeded
    if not _random_seeded:
        random.seed()  # uses cur system time
        _random_seeded = True

    while True:
        yield random.randrange(2, max)


def rabinmiller(n: int, *, numtrials: int = 200) -> bool:
    """
    Tests if a number is PROBABLY prime, by running the strong fermat test 
    many times with random bases from 2 to n-1
    n: The number to test
    numtrials: The number of bases to try with the strong fermat test
    
    if numtrials is 200, the chance of a false positive is 4*10^-121
    """
    gen = _randiter(n)
    for _ in range(numtrials):
        base = next(gen)
        if not strongfermat(n, base):
            return False

    return True
