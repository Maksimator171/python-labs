import unittest
from rsa import is_prime, gcd, multiplicative_inverse, generate_keypair

class TestRSA(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertTrue(is_prime(13))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(10, 0), 10)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        e, phi = 7, 40
        d = multiplicative_inverse(e, phi)
        self.assertEqual((e * d) % phi, 1)

    def test_generate_keypair(self):
        public, private = generate_keypair(17, 19)
        e, n = public
        d, n2 = private
        self.assertEqual(n, n2)
        self.assertEqual((e * d) % ((17-1)*(19-1)), 1)