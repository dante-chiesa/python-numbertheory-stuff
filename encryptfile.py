#!/usr/bin/python3

import filetonums
from modexp import modexp
from typing import List, NamedTuple

class EncNums(NamedTuple):
    nums: List[int]
    padding: int
    N: int
    e: int

    def __str__(self):
        res = ""
        res += f"padding:{self.padding}\n"
        res += f"N:{self.N}\n"
        res += f"e:{self.e}\n"
        res += "DATA:\n"
        for n in self.nums:
            res += f"{n}\n"
        return res

    def to_file(self, filename: str):
        with open(filename, "wt") as f:
            f.write(str(self))

def _encryptnum(x: int, N: int, exp:int) -> int:
    return modexp(x, modulo=N, exp=exp)

def encryptfile(filename: str, N: int, exp: int):
    filenums: filetonums.FileNums = filetonums.filetonums(filename)
    return encryptfilenums(filenums, N, exp)

def encryptfilenums(filenums: filetonums.FileNums, N: int, exp: int):
    encnums: List[int] = [_encryptnum(n, N, exp) for n in filenums.nums]
    return EncNums(encnums, filenums.padding, N, exp)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} infile N exp [outfile]")
        print("(no outfile to print to stdout)")
    else:
        file = sys.argv[1]
        N= int(sys.argv[2])
        exp= int(sys.argv[3])
        res = encryptfile(file, N, exp)
        if len(sys.argv) >= 5:
            res.to_file(sys.argv[4])
        else:
            print(str(res))
