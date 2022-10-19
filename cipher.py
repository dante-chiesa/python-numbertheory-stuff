#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361
from multinv import multinv


def _chartonum(c):
    num = ord(c)
    # we lowercase all strings so this works
    return num - ord("a")


def _numtochar(n):
    n += ord("a")
    return chr(n)


def caesarencode(offset, text):
    return affineencode(1, offset, text)


def caesardecode(offset, text):
    return affinedecode(1, offset, text)


def affineencode(alpha, beta, text):
    """
    Affineencodes the text in an affine cipher
    x -> alpha * x + beta (mod 26)
    """
    text = text.lower()
    resultchars = []
    for c in text:
        num = _chartonum(c)
        num = (alpha * num + beta) % 26
        resultchars.append(_numtochar(num))

    return "".join(resultchars)


def affinedecode(alpha, beta, text):
    """
    Affinedecodes text which was affineencoded by an affine cipher with arguments a and b
    """
    alphainv = multinv(alpha, 26)
    if alphainv == "NaN":
        return "Cannot be affinedecoded, alpha is not relatively prime with 26"
    betainv = (alphainv * -beta) % 26
    return affineencode(alphainv, betainv, text)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 5 or (sys.argv[1] != "enc" and sys.argv[1] != "dec"):
        print('Usage: cipher.py [enc|dec] a b "str"')
    else:
        alpha = int(sys.argv[2])
        beta = int(sys.argv[3])
        text = sys.argv[4]
        if sys.argv[1] == "enc":
            print(affineencode(alpha, beta, text))
        elif sys.argv[1] == "dec":
            print(affinedecode(alpha, beta, text))
        else:
            print("Error: Unknown mode!")
