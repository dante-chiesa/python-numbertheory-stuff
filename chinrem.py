#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361
import euclid
from functools import reduce
from multinv import multinv


def _allrelativelyprime(modpairs):
    """
    checks if all modulo bases in the set are relatively prime with each other
    """
    for i in range(0, len(modpairs)):
        m1 = modpairs[i][1]
        for j in range(i + 1, len(modpairs)):
            m2 = modpairs[j][1]
            if euclid.gcd(m1, m2) != 1:
                return False
    return True


def chinrem(modpairs):
    """
    applies the chinese remainder theorem to solve a system of equations
    of the type:
    X = a1 (mod m1)
    X = a2 (mod m2), etc
    """
    if not _allrelativelyprime(modpairs):
        return "Not solvable by this algorithm, some moduli are not relatively prime"
    productM = reduce((lambda x, y: x * y[1]), modpairs, 1)
    sumA = 0
    for pair in modpairs:
        a_n, m_n = pair
        M_n = productM // m_n
        b_n = multinv(M_n, m_n)
        sumA += a_n * b_n * M_n

    sumA = sumA % productM
    return {"x_equals": sumA, "mod": productM}


def prettyprint(modpair):
    if isinstance(modpair, str):
        return modpair  # pass error messages through
    a = modpair["x_equals"]
    m = modpair["mod"]
    return "X === " + str(a) + " (mod " + str(m) + ")"


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 5 or len(sys.argv) % 2 != 1:
        print(
            "Usage: chinrem.py x1 mod1 x2 mod2 [x3 mod3...]\n"
            + "to solve X = x1 mod mod1, X = x2 mod mod2..."
        )
    else:
        pairs = []
        i = 1
        while i < len(sys.argv):
            a = int(sys.argv[i])
            m = int(sys.argv[i + 1])
            pairs.append((i, m))
            i += 2
        print(prettyprint(chinrem(pairs)))
