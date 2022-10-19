#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361

from texttonum import numtotext, texttonum, partition
from mathfns import multinv, modexp
import diffie_helman as dh
import math


def ELGencrypt_raw(text, pub_val, priv_exp, root, prime, blocksize=None):
    """
    Encrypts a text by the ElGamal encryption scheme. 
    'root' must be a primitive root of 'prime'
    If blocksize is not specified, it is set automatically
    Returns an array of intermediate encryption results
    """
    if blocksize is None:
        blocksize = math.floor(math.log(prime, 100))

    privkey = dh.privatekey(pub_val, priv_exp, prime)
    pubkey = dh.pubvalfromexp(priv_exp, root, prime)

    blocks = partition(text, blocksize)
    data = []
    for block in blocks:
        num = texttonum(block)
        encodednum = num * privkey % prime
        data.append({"text": block, "num": num, "encrypted": encodednum})
    return {"pubkey": pubkey, "data": data}


def ELGencrypt(text, pub_val, priv_exp, root, prime, blocksize=None):
    """
    Encrypts a text by the ElGamal encryption scheme. 
    'root' must be a primitive root of 'prime'
    If blocksize is not specified, it is set automatically
    Returns only the data needed for decryption
    """

    result = ELGencrypt_raw(text, pub_val, priv_exp, root, prime, blocksize)
    encryptedblocks = [x["encrypted"] for x in result["data"]]
    return {"pubkey": result["pubkey"], "blocks": encryptedblocks}


def ELGdecrypt_raw(payload, priv_exp, prime):
    """
    Dencrypts a text by the ElGamal encryption scheme. 
    Returns an array of intermediate decryption results
    """
    privkey = dh.privatekey(payload["pubkey"], priv_exp, prime)
    privinv = multinv(privkey, prime)
    data = []
    for block in payload["blocks"]:
        decrypted = block * privinv % prime
        text = numtotext(decrypted)
        data.append({"num": block, "decrypted": decrypted, "text": text})
    return data


def ELGdecrypt(payload, priv_exp, prime):
    """
    Dencrypts a text by the ElGamal encryption scheme. 
    Returns only the decrypted text
    """
    data = ELGdecrypt_raw(payload, priv_exp, prime)
    text = "".join((x["text"] for x in data))
    return text

def ELGdecrypt_fromparts(blocks, pubkey, priv_exp, prime):
    payload = {"pubkey":pubkey,"blocks":blocks}
    return ELGdecrypt(payload, priv_exp, prime)
