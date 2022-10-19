#!/usr/bin/python3

import math

MAX_LOOP = 10**6

def _squaregen(start):
    a = start
    asquared = a * a
    while True:
        yield (a, asquared)
        asquared += 2*a + 1
        a += 1
    

def fermatfactor_raw(n):
    if n % 2 == 0:
        raise ArithmeticError(f"n ({n}) must not be divisible by 2")

    sqrtn = math.ceil(math.sqrt(n))
    lowgen = _squaregen(0)
    highgen = _squaregen(sqrtn)

    low, lowsq = next(lowgen)
    high, highsq = next(highgen)

    #start at 1 because the first comparison counts
    lowsteps = 1;
    highsteps = 1;
    while not lowsq + n == highsq:
        if lowsteps > MAX_LOOP and highsteps > MAX_LOOP:
            raise ArithmeticError(f"More than {MAX_LOOP} iterations, aborted factorization")
        if lowsq >= highsq:
            raise ArithmeticError("unknown error, cannot factor")
        if (lowsq + n < highsq):
            low, lowsq = next(lowgen)
            lowsteps += 1
        else:
            high, highsq = next(highgen)
            highsteps += 1

    return {"highsteps": highsteps, "lowsteps": lowsteps, "a": high, "b":low,
            "a-b":high - low, "a+b": high+low}



def fermatfactor(n):
    pow2 = 0
    while n % 2 == 0:
        pow2 += 1
        n = n //2

    res = []
    if pow2 != 0:
        res.append((2, pow2))

    if n == 1:
        return res

    sqrtn = math.ceil(math.sqrt(n))
    if sqrtn * sqrtn == n: # perfect square
        res.append((sqrtn, 2))
        return res;

    fermatres = fermatfactor_raw(n)
    res.extend([(fermatres["a-b"], 1), (fermatres["a+b"],1)])
    return res
