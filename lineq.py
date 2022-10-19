#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361
import euclid
import math


def _simplifysolution(sln):
    # normalize so x t coefficent is always positive
    if sln["x_tcoeff"] < 0:
        sln["x_tcoeff"] *= -1
        sln["y_tcoeff"] *= -1
    # TODO currently finds min positive x0,
    # but could find x,y closest to origin
    delta_t = -1 * math.floor(sln["x0"] / sln["x_tcoeff"])
    sln["x0"] += delta_t * sln["x_tcoeff"]
    sln["y0"] += delta_t * sln["y_tcoeff"]
    return sln


def lineq(xcoeff, ycoeff, c):
    """
    finds all integer solutions to the equation
    x * xcoeff + y * ycoeff = c
    """
    gcd = euclid.gcd(xcoeff, ycoeff)
    if c % gcd != 0:
        return "No solutions"
    xreduced, yreduced, creduced = xcoeff // gcd, ycoeff // gcd, c // gcd
    x1, y1 = euclid.xyfromtable(euclid.euclid(xreduced, yreduced))
    if xcoeff < ycoeff:
        x1, y1 = y1, x1  # the coefficient for the larger value is always first
    x0, y0 = x1 * creduced, y1 * creduced
    x_tcoeff = yreduced
    y_tcoeff = -xreduced
    solution = {
        "x0": int(x0),
        "y0": int(y0),
        "x_tcoeff": int(x_tcoeff),
        "y_tcoeff": int(y_tcoeff),
    }
    return _simplifysolution(solution)


def formatsolution(sln):
    if sln == "No solutions":
        return sln
    xstr = "x = " + str(int(sln["x0"])) + " + " + str(int(sln["x_tcoeff"])) + "t"
    ystr = "y = " + str(int(sln["y0"]))
    if sln["y_tcoeff"] < 0:
        ystr += " - " + str(-int(sln["y_tcoeff"])) + "t"
    else:
        ystr += " + " + str(int(sln["y_tcoeff"])) + "t"

    return xstr + "\n" + ystr


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print(
            """Usage: to solve "x * xcoeff + y * ycoeff = c":\nlineq.py xcoeff ycoeff c"""
        )
    else:
        xcoeff = int(sys.argv[1])
        ycoeff = int(sys.argv[2])
        c = int(sys.argv[3])
        print(formatsolution(lineq(xcoeff, ycoeff, c)))
