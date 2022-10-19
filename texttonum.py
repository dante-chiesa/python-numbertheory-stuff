# Created by Dante Chiesa for Professor B________, Math 361

_INVALID_CHAR = "\uFFFD"

_chartonum_dict = {
    "a": 11,
    "b": 12,
    "c": 13,
    "d": 14,
    "e": 15,
    "f": 16,
    "g": 17,
    "h": 18,
    "i": 19,
    "j": 20,
    "k": 21,
    "l": 22,
    "m": 23,
    "n": 24,
    "o": 25,
    "p": 26,
    "q": 27,
    "r": 28,
    "s": 29,
    "t": 30,
    "u": 31,
    "v": 32,
    "w": 33,
    "x": 34,
    "y": 35,
    "z": 36,
    "A": 37,
    "B": 38,
    "C": 39,
    "D": 40,
    "E": 41,
    "F": 42,
    "G": 43,
    "H": 44,
    "I": 45,
    "J": 46,
    "K": 47,
    "L": 48,
    "M": 49,
    "N": 50,
    "O": 51,
    "P": 52,
    "$Q": 53,
    "R": 54,
    "S": 55,
    "T": 56,
    "U": 57,
    "V": 58,
    "W": 59,
    "X": 60,
    "Y": 61,
    "Z": 62,
    "0": 63,
    "1": 64,
    "2": 65,
    "3": 66,
    "4": 67,
    "5": 68,
    "6": 69,
    "7": 70,
    "8": 71,
    "9": 72,
    ".": 73,
    ",": 74,
    "!": 75,
    "?": 76,
    ":": 77,
    ";": 78,
    "=": 79,
    "+": 80,
    "-": 81,
    "*": 82,
    "/": 83,
    "^": 84,
    "\\": 85,
    "@": 86,
    "#": 87,
    "&": 88,
    "(": 89,
    ")": 90,
    "[": 91,
    "]": 92,
    "{": 93,
    "}": 94,
    "$": 95,
    "%": 96,
    "_": 97,
    "'": 98,
    " ": 99,
}

_numtochar_dict = {
    11: "a",
    12: "b",
    13: "c",
    14: "d",
    15: "e",
    16: "f",
    17: "g",
    18: "h",
    19: "i",
    20: "j",
    21: "k",
    22: "l",
    23: "m",
    24: "n",
    25: "o",
    26: "p",
    27: "q",
    28: "r",
    29: "s",
    30: "t",
    31: "u",
    32: "v",
    33: "w",
    34: "x",
    35: "y",
    36: "z",
    37: "A",
    38: "B",
    39: "C",
    40: "D",
    41: "E",
    42: "F",
    43: "G",
    44: "H",
    45: "I",
    46: "J",
    47: "K",
    48: "L",
    49: "M",
    50: "N",
    51: "O",
    52: "P",
    53: "$Q",
    54: "R",
    55: "S",
    56: "T",
    57: "U",
    58: "V",
    59: "W",
    60: "X",
    61: "Y",
    62: "Z",
    63: "0",
    64: "1",
    65: "2",
    66: "3",
    67: "4",
    68: "5",
    69: "6",
    70: "7",
    71: "8",
    72: "9",
    73: ".",
    74: ",",
    75: "!",
    76: "?",
    77: ":",
    78: ";",
    79: "=",
    80: "+",
    81: "-",
    82: "*",
    83: "/",
    84: "^",
    85: "\\",
    86: "@",
    87: "#",
    88: "&",
    89: "(",
    90: ")",
    91: "[",
    92: "]",
    93: "{",
    94: "}",
    95: "$",
    96: "%",
    97: "_",
    98: "'",
    99: " ",
}


def _chartonum(c):
    if not c in _chartonum_dict:
        raise Exception("illegal character, can't be encrypted")
    return _chartonum_dict[c]


def _numtochar(n):
    if not n in _numtochar_dict:
        #raise Exception(f"illegal number {n}, can't be decrypted")
        return _INVALID_CHAR
    return _numtochar_dict[n]


def _joinnums(numarray):
    arrlen = len(numarray)
    result = 0
    for i in range(1, arrlen + 1):
        result += numarray[-i] * 100 ** (i - 1)
    return result


def _splitnum(num):
    nums = []
    while num > 0:
        nums.append(num % 100)
        num = num // 100
    nums.reverse()
    return nums


def texttonum(text):
    numarray = [_chartonum(c) for c in text]
    return _joinnums(numarray)


def numtotext(num):
    numarray = _splitnum(num)
    return "".join([_numtochar(n) for n in numarray])

def partition(arr, blocksize):
    """
    Splits a list into a list-of-lists, each with length blocksize
    """
    totallen = len(arr)
    result = []
    idx = 0
    while idx < totallen:
        # slicing beyond end is safe, just clamps to end
        result.append(arr[idx : idx + blocksize])
        idx += blocksize
    return result
