#!/usr/bin/python3
# Created by Dante Chiesa for Professor B________, Math 361

import unittest


class ModExpTestCase(unittest.TestCase):
    def test_modexp(self):
        from modexp import modexp

        self.assertEqual(modexp(12, 13, 79), 78)
        self.assertEqual(modexp(123, 456, 789), 699)
        self.assertEqual(modexp(123454321, 222333222, 133313331), 54340384)
        self.assertEqual(
            modexp(112233445566778899, 1213141516171819, 111333555333111),
            56223913841334,
        )


class EuclidTestCase(unittest.TestCase):
    def setUp(self):
        import euclid

        self.table = euclid.euclid(13566, 4620)

    def test_GCD(self):
        import euclid

        self.assertEqual(euclid.gcdfromtable(self.table), 42)

    def test_XY(self):
        import euclid

        x, y = euclid.xyfromtable(self.table)
        self.assertEqual((x, y), (47, -138))


class SieveTestCase(unittest.TestCase):
    def test_sieve1(self):
        from sieve import sieve

        primes = sieve(100, 260)
        self.assertEqual(len(primes), 30)
        self.assertEqual(primes[0], 101)
        self.assertEqual(primes[11], 157)
        self.assertEqual(primes[29], 257)

    def test_sieve2(self):
        from sieve import sieve

        primes = sieve(601, 1010)
        self.assertEqual(len(primes), 60)
        self.assertEqual(primes[0], 601)
        self.assertEqual(primes[59], 1009)
        self.assertEqual(primes[23], 751)


class TrialDivisionTestCase(unittest.TestCase):
    def test_trialdiv(self):
        from trialdivision import trialdivision

        res = trialdivision(133331)
        self.assertEqual(res.remaining, None)
        self.assertEqual(res.factors, [(11, 1), (17, 1), (23, 1), (31, 1)])

    def test_trialdiv2(self):
        from trialdivision import trialdivision

        a = 3907
        b = 5147
        pa = 10
        pb = 7
        res = trialdivision((a ** pa) * (b ** pb))
        self.assertEqual(res.remaining, None)
        self.assertEqual(res.factors, [(a, pa), (b, pb)])

    def test_unfactorable(self):
        from trialdivision import trialdivision

        largeprime = 1270270911464117
        res = trialdivision(largeprime)
        self.assertEqual(len(res.factors), 0)
        self.assertEqual(res.remaining, largeprime)


class LinEqSolverTestCase(unittest.TestCase):
    def test_lineq(self):
        from lineq import lineq

        sln = lineq(30, 50, 70)
        realsln = {"x0": 4, "y0": -1, "x_tcoeff": 5, "y_tcoeff": -3}
        self.assertEqual(sln, realsln)

    def test_lineq2(self):
        from lineq import lineq

        sln = lineq(42, -30, 12)
        realsln = {"x0": 1, "y0": 1, "x_tcoeff": 5, "y_tcoeff": 7}
        self.assertEqual(sln, realsln)

    def test_unsolvable(self):
        from lineq import lineq

        sln = lineq(2, 2, 3)
        self.assertEqual(sln, "No solutions")


class MultInvTestCase(unittest.TestCase):
    def test_multinv(self):
        from multinv import multinv

        self.assertEqual(multinv(17, 23), 19)
        self.assertEqual(multinv(123456789, 1333133313331), 858367108549)
        self.assertEqual(multinv(2, 4), "NaN")


class ChinRemTestCase(unittest.TestCase):
    def test_chinrem1(self):
        from chinrem import chinrem

        pairs = [(1, 3), (2, 5)]
        expectedresult = {"x_equals": 7, "mod": 15}
        self.assertEqual(chinrem(pairs), expectedresult)

    def test_chinremunsolvable(self):
        from chinrem import chinrem

        pairs = [(1, 2), (3, 4)]
        self.assertEqual(
            chinrem(pairs),
            "Not solvable by this algorithm, some moduli are not relatively prime",
        )


class TextToNumTestCase(unittest.TestCase):
    helloworldnum = 441522222599592528221475

    def test_texttonum(self):
        from texttonum import texttonum

        text = "Hello World!"
        num = texttonum(text)
        self.assertEqual(num, self.helloworldnum)

    def test_numtotext(self):
        from texttonum import numtotext

        num = self.helloworldnum
        text = numtotext(num)
        self.assertEqual(text, "Hello World!")


class OrderTestCase(unittest.TestCase):
    def test_order(self):
        from order import order

        self.assertEqual(order(5, 28), 6)
        self.assertEqual(order(19, 1333331), 1333330)


class RSATestCase(unittest.TestCase):
    # both primes
    N = 9001 * 9929
    # must be relatively prime with phi(N)
    e = 127
    text = "adkfsjaklgj 234829875 adf!!@z78"
    # N is only large enough for blocksize of 3
    blocksize = 3

    def test_encdec(self):
        import rsa

        encr = rsa.rsaencrypt(self.text, self.N, self.e, self.blocksize)
        decr = rsa.rsadecrypt_brute(encr, self.N, self.e)
        # decrypting yiels the encrypted text
        self.assertEqual(self.text, decr)


class BaseConvertTestCase(unittest.TestCase):
    num = 2 ** 10 + 2 ** 7 + 2 ** 5 + 2 ** 2
    # result is lowest-bit first in array, so reverse the list
    numbits = [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0][::-1]

    def test_base2(self):
        from baseconvert import baseconvert

        bits = baseconvert(self.num, 2)
        self.assertEqual(bits, self.numbits)


class CipherTestCase(unittest.TestCase):
    def test_caesarenc(self):
        import cipher

        self.assertEqual(cipher.caesarencode(13, "abcd"), "nopq")

    def test_caesardec(self):
        import cipher

        text = "helloWORLD"
        enc = cipher.caesarencode(25, text)
        dec = cipher.caesardecode(25, enc)
        # doesn't preserve case
        self.assertNotEqual(dec, text)
        self.assertEqual(dec, text.lower())


class PhiTestCase(unittest.TestCase):
    # no test to ensure arbitrary-precision accuracy because the trialdivision on which
    # phi depends cannot factor such large numbers, unfortunately
    q = 9929  # prime
    p = 9001  # prime
    N = p * q
    phi_N = N * (1 - 1 / p) * (1 - 1 / q)

    def test_phi_compound(self):
        from phi import phi

        self.assertEqual(phi(self.N), self.phi_N)

    def test_phi_prime(self):
        from phi import phi

        self.assertEqual(phi(self.p), self.p - 1)

    def test_phi_precision(self):
        from phi import phi
        from modexp import modexp

        large_N = (self.p ** 5) * (self.q ** 11)
        random_base = 231798137209783978

        # any number to the power of phi(N) equals 1 mod N
        result = modexp(random_base, phi(large_N), large_N)
        self.assertEqual(result, 1)


class IndexTestCase(unittest.TestCase):
    def test_index_brute(self):
        prime = 37
        root = 2
        from index import index_brute

        x = 5
        idx = index_brute(root ** x % prime, root, prime)
        self.assertEqual(x, idx)

    def test_babygiant(self):
        prime = 1993
        root = 23
        from index import index_babygiant

        x = 11
        res = index_babygiant(root ** x % prime, root, prime)
        self.assertEqual(x, res["i+Nj"])


class DiffieHelmanTestCase(unittest.TestCase):
    def test_dh_symmetric(self):
        import diffie_helman as dh

        prime = 1993
        root = 23
        exp_a = 234
        exp_b = 327

        pub_a = dh.pubvalfromexp(exp_a, root, prime)
        pub_b = dh.pubvalfromexp(exp_b, root, prime)
        key_a = dh.privatekey(pub_b, exp_a, prime)
        key_b = dh.privatekey(pub_a, exp_b, prime)
        self.assertEqual(key_a, key_b)

    def test_dh_values(self):
        import diffie_helman as dh
        from modexp import modexp

        prime = 2081
        root = 1214
        exp_a = 111
        exp_b = 789

        pub_a = dh.pubvalfromexp(exp_a, root, prime)
        key = dh.privatekey(pub_a, exp_b, prime)
        self.assertEqual(key, modexp(root, exp_a * exp_b, prime))


class ElGamalTestCase(unittest.TestCase):
    def test_elg_symmetric(self):
        import diffie_helman as dh
        import elgamal as elg

        prime = 2081
        root = 1214
        exp_a = 111
        exp_b = 789
        text = "Testing Testing 123..."
        pub_a = dh.pubvalfromexp(exp_a, root, prime)

        encrypted = elg.ELGencrypt(text, pub_a, exp_b, root, prime)
        decrypted = elg.ELGdecrypt(encrypted, exp_a, prime)
        self.assertEqual(text, decrypted)


class StrongFermatTestCase(unittest.TestCase):
    def test_strong_fermat(self):
        from strongfermat import strongfermat
        from sieve import sieve

        maxnum = 1000

        # this part is true for any range
        primes = sieve(2, maxnum)
        allprimesareprime = all(strongfermat(x, 2) for x in primes)
        self.assertTrue(allprimesareprime)

        # this is not necessarily true, may have false positives
        allcompositesarecomposite = not any(
            strongfermat(x, 2) for x in range(2, maxnum) if x not in primes
        )
        self.assertTrue(allcompositesarecomposite)


class RabinMillerTestCase(unittest.TestCase):
    def test_rabin_miller(self):
        from rabinmiller import rabinmiller

        primenum = 1270270911464117
        compnum = 1270270911464119

        self.assertTrue(rabinmiller(primenum))
        self.assertFalse(rabinmiller(compnum))


class PollardTestCase(unittest.TestCase):
    def test_pollard_rho(self):
        from pollard import rhomethod

        p = 77377
        q = 3799973
        compnum = p * q

        ans = rhomethod(compnum, fun=lambda x: x ** 2 + 1, x_0=2, max_iter=1000)

        assertTrue(compnum % ans == 0)
        assertEqual(ans, p)

    def test_pollard_p_minus_one(self):
        from pollard import pminusonemethod

        p = 77377
        q = 3799973
        compnum = p * q

        ans = pminusonemethod(compnum, x_0=2, max_iter=1000)
        self.assertTrue(compnum % ans == 0)
        self.assertEqual(ans, p)


class MyPyTestCase(unittest.TestCase):
    def test_run_mypy(self):
        import os

        curdir = os.getcwd()
        with os.popen(f"mypy {curdir}") as pipe:
            output = pipe.read()
            self.assertEqual(output, "")


if __name__ == "__main__":
    unittest.main()
