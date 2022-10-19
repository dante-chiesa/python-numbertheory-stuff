#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361

# math.log, math.floor
import math


def _matmult2d(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                c[i][j] += a[i][k] * b[k][j]
    return c


def _calcxy(table):
    mat = [[1, 0], [0, 1]]
    for line in table:
        q = line[1]
        tempmat = [[0, 1], [1, -q]]
        mat = _matmult2d(tempmat, mat)
    return (mat[0][0], mat[0][1])


def prettyprint(table):
    maxlen = 1
    for line in table:
        for num in line:
            len = 1
            if num < 0:
                len += 1
                num = -num
            if num == 0:
                continue
            len += math.floor(math.log(num, 10))
            if len > maxlen:
                maxlen = len

    for line in table:
        fmt = "{0:" + str(maxlen) + "d}"
        linestr = " ".join(fmt.format(x) for x in line)
        linestr = "[ " + linestr + " ]"
        print(linestr)


def euclid(a, b):
    """
    Calculates the gcd of a and b by Euclid's algorithm.
    Final line of the table represents x * a + y * b = gcd
    """
    if b > a:
        return euclid(b, a)

    initiala = a
    initialb = b
    table = []
    done = False
    while not done:
        q = a // b
        r = a - q * b
        if r < 0:  # ensure no negative r
            sign = 1 if b >= 0 else -1
            r += sign * b
            q -= sign * 1
        if r == 0:
            done = True
        table.append([a, q, b, r, 0])
        a = b
        b = r

    x, y = _calcxy(table)
    table.append([x, initiala, y, initialb, x * initiala + y * initialb])
    return table


def gcdfromtable(table):
    return table[-2][2]


def gcd(a, b):
    return gcdfromtable(euclid(a, b))


def xyfromtable(table):
    [x, _, y, _, _] = table[-1]
    return (x, y)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: euclid.py a b")
    else:
        prettyprint(euclid(int(sys.argv[1]), int(sys.argv[2])))
