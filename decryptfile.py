#!/usr/bin/python3

import filetonums
from modexp import modexp
from typing import List, NamedTuple
from encryptfile import EncNums
from filetonums import FileNums, numstofile
import re

_default_N = 919441817365150968707373412828889627995081
_default_d = 596584385313265895724912909090298796787511
_default_e = 131

def file_to_encnums(filename:str):
    N = None
    e = None
    padding = None

    with open(filename, "rt") as f:
        line = next(f).strip().split(":", 1)
        while True:
            if re.search(r"\bN\b", line[0], re.IGNORECASE):
                N = int(line[1])
                pass
            elif re.search(r"\bpadding\b", line[0], re.IGNORECASE):
                padding = int(line[1])
                pass
            elif re.search(r"\be\b", line[0], re.IGNORECASE):
                e = int(line[1])
                pass
            elif re.search(r"data", line[0], re.IGNORECASE):
                break # end of header

            line = next(f).strip().split(":", 1)

        if N is None: N = _default_N
        if e is None: d = _default_d
        if padding is None: padding = 0

        nums = [int(n) for n in f]
        return EncNums(nums, padding, N, e)
    

def decrypt_encnums(encnums:EncNums, d: int):
    newnums = [modexp(n, exp=d, modulo=encnums.N) for n in encnums.nums]
    return FileNums(newnums, encnums.padding)

def decrypt_file(filename:str, d:int):
    return decrypt_encnums(file_to_encnums(filename), d)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print(f"Usage: {argv[0]} infile d outfile\n")
        print("pass _ as d to use default")
    else:
        infile = sys.argv[1]
        d = None
        if (sys.argv[2] == "_"):
            d = _default_d
        else:
            d= int(sys.argv[2])
        outfile = (sys.argv[3])

        decrypt_file(infile, d).to_file(outfile)
