#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361
from mathfns import multinv, modexp


def pubvalfromexp(private_exp,root,prime):
    """ 
    Generates a public value to exchange over the wire in Diffie-Helman key exchange.
    The exponent used to generate this value must be kept secret, though the prime
    and its primitive root may be public
    """
    return modexp(root,private_exp,prime)

def privatekey(pub_val, private_exp, prime):
    """
    Generates a secret key by Diffie-Helman key exchange, from your secret exponent
    And your partner's public value (equal to root^exp mod prime)
    """
    return modexp(pub_val,private_exp, prime)
    
