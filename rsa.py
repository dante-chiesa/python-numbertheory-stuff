#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361

from texttonum import numtotext, texttonum, partition
from multinv import multinv
from modexp import modexp
from phi import phi

# rsa encryption algorithm with prime N, exponent e, blocksize n
# divide text into blocksof n characters, convert to number, calc modexp(num,e,N)
# to decrypt, just modexp (num,d,N), where d= multinv(e, phi(N))
# for real RSA, N = p,q, phi calculated from thse prime factors
# for now we have low N and can factorize on the fly


def _calculate_d(prime, exp):
    """
    Calculates d such that d * `e` === 1 (mod phi(`N`)).
    Requires prime factorization, so for true rsa keys this is stored
    in the private key rather than calculated
    """
    return multinv(exp, phi(prime))

def rsaencrypt_raw(text, N, exp, blocksize):
    """
    Splits the text into blocks and returns a n array containing
    the pre-encryption block, numerical translation of that text bloc, and 
    post-encryption number.
    """
    blocks = partition(text, blocksize)
    result = []
    for block in blocks:
        num = texttonum(block)
        encodednum = modexp(num, exp, N)
        result.append({"text": block, "num": num, "encrypted": encodednum})
    return result


def rsaencrypt(text, N, exp, blocksize):
    """
    Encrypts a number in RSA with `N` as the modulus and `exp` as the exponent, splitting
    the text into size blocksize. `blocksize` must be less than log_100(N) or data
    loss will result
    """
    data = rsaencrypt_raw(text, N, exp, blocksize)
    nums = [x["encrypted"] for x in data]
    return nums


def rsadecrypt_raw(block_list, N, d_exp):
    """
    Decrypts an array of numbers into text by RSA, and returns
    an array of intermediate results.
    The text must have been encoded according to `texttonum`
    """
    result = []
    for blocknum in block_list:
        decodednum = modexp(blocknum, d_exp, N)
        text = numtotext(decodednum)
        result.append({"num": blocknum, "decrypted": decodednum, "text": text})
    return result


def rsadecrypt_brute_raw(block_list, N, e_exp):
    """
    Same as rsaencrypt_raw, but it calculates d by prime factorization from e.
    Impossible for sufficiently large N.
    """
    d_exp = _calculate_d(N, e_exp)
    return rsadecrypt_raw(block_list, N, d_exp)


def rsadecrypt_brute(block_list, N, e_exp):
    """
    Same as rsaencrypt, but it calculates d by prime factorization from e.
    Impossible for sufficiently large N.
    """
    d_exp = _calculate_d(N, e_exp)
    d_exp = _calculate_d(N, e_exp)
    data = rsadecrypt_raw(block_list, N, d_exp)
    return "".join([d["text"] for d in data])


def rsadecrypt(block_list, N, d_exp):
    """
    Decrypts a list of numbers into the text they represent. `N` is the modulus, and 
    `d_exp` is the decryption exponent from the private key.
    The text must have been encoded according to `texttonum`
    """
    data = rsadecrypt_raw(block_list, N, d_exp)
    return "".join([d["text"] for d in data])


if __name__ == "__main__":
    helpstring = "Usage: rsa.py [args] TODO"
    import sys

    arglen = len(sys.argv)
    if arglen < 3:
        print(helpstring)
    elif sys.argv[1] == "enc":
        pass
    elif sys.argv[1] == "dec":
        pass
