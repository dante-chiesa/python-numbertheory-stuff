#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361

import math


def next_nonnull(list, idx, max):
    idx = idx + 1
    while list[idx] is None and idx < max:
        idx += 1
    if idx >= max:
        idx = -1
    return idx


def sieve(begin, end):
    """
    Calculates primes between begin and end by the sieve of eratosthenes
    """
    nums = [x for x in range(0, end + 1)]
    nums[0] = None
    nums[1] = None
    cur_index = 2
    max_index = 1 + math.floor(math.sqrt(end))
    while cur_index < max_index and cur_index != -1:
        cur_prime = nums[cur_index]
        index2 = cur_index + cur_prime
        while index2 <= end:
            nums[index2] = None
            index2 += cur_prime
        cur_index = next_nonnull(nums, cur_index, max_index)

    return [x for x in nums if x is not None and x >= begin]


def prettyprint(nums, delim):
    print(delim.join([str(x) for x in nums]))


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: sieve.py min max [delimiter]")
    else:
        begin = int(sys.argv[1])
        end = int(sys.argv[2])
        delim = ", "
        if len(sys.argv) >= 4:
            delim = sys.argv[3]
        prettyprint(sieve(begin, end), delim)
