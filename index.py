#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361
from math import ceil, sqrt
from multinv import multinv
from phi import phi


def index_brute(a, root, modulus):
    """
    Calculates the index by brute force, texting every exponent for root
    and comparing to a
    """
    if a >= modulus or a < 0:
        raise ArithmeticError(f"{a} not within [0,{modulus})")

    exp = 0
    current_val = 1  # root^0

    # todo is max value modulus - 1 or phi(modulus)?
    # same for primes but different otherwise
    while exp < modulus:
        if current_val == a:
            return exp
        current_val = current_val * root % modulus
        exp += 1

    # reached end without finding an index
    raise ArithmeticError(f"{a} has no index base {root} mod {modulus}")


def index_babygiant(a, root, modulus):
    """ 
    Calculates the index by the baby-step giant-step method, which is faster
    than brute force for large numbers
    """
    if a >= modulus or a < 0:
        raise ArithmeticError(f"{a} not within [0,{modulus})")

    N = ceil(sqrt(modulus - 1))

    i_val = 1
    i_dict = {i_val: 0}  # dict of val:exp
    for i in range(1, N):
        i_val = i_val * root % modulus
        i_dict[i_val] = i

    j_factor = multinv(root ** N, modulus)  # r^-N
    j_val = a
    j_dict = {j_val: 0}
    for j in range(1, N):
        j_val = j_val * j_factor % modulus
        j_dict[j_val] = j

    i_value_set = set((x for (x, _) in i_dict.items()))
    j_value_set = set((x for (x, _) in j_dict.items()))

    intersect = i_value_set.intersection(j_value_set)
    if len(intersect) < 1:
        raise ArithmeticError(f"{a} has no index base {root} mod {modulus}")
    # if len(intersect) > 1:
    #     #TODO is multiple intersections legal?
    #     print("Multiple intersections:")
    #     for intersect_val in intersect:
    #         i = i_dict[intersect_val]
    #         j = j_dict[intersect_val]
    #         exp = (i + j * N) % phi(modulus)
    #         result_dict = {"i":i, "j": j, "intersection":intersect_val, "i+Nj": exp}
    #         print(f"{result_dict!r}")
    #     print("-----")

    # raise ArithmeticError(
    #    f"{a} has more than one index base {root} mod {modulus}, somehow:\n"
    #    + f"intersections: {intersect!r}")

    intersect_val = intersect.pop()  # arbitrary element from set

    # exp = i + jN
    i = i_dict[intersect_val]
    j = j_dict[intersect_val]
    exp = (i + j * N) % phi(modulus)
    result_dict = {"i": i, "j": j, "intersection": intersect_val, "i+Nj": exp}

    return result_dict


def index(a, root, modulus):
    """
    Calculates the index of 'n' base 'root' mod 'modulus', 
    i.e. the exponent such that root^exp === n (mod modulus)
    root must actually be a primitive root of the modulus
    """

    # return index_brute(a, root, modulus)
    result = index_babygiant(a, root, modulus)
    return result["i+Nj"]


if __name__ == "__main__":
    from sys import argv

    if len(argv) < 4:
        print(
            "Usage: index.py a root modulus\n" + "to solve root ^ x = a (mod modulus)"
        )
    else:
        a = int(argv[1])
        root = int(argv[2])
        modulus = int(argv[3])
        print(index(a, root, modulus))
