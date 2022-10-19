# Created by Dante Chiesa for Professor B________, Math 361


def baseconvert(val, base):
    """
    Converts base-10 number `val` to  base `base`.
    result will be a little-endian array of digits
    """
    digits = []
    while val > 0:
        digits.append(val % base)
        val = val // base
    return digits
