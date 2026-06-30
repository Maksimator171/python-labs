import unittest
from caesar import encrypt_caesar, decrypt_caesar

class TestCaesar(unittest.TestCase):
    def test_encrypt_default_shift(self):
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")
        self.assertEqual(encrypt_caesar(""), "")

    def test_encrypt_custom_shift(self):
        self.assertEqual(encrypt_caesar("ABC", 1), "BCD")
        self.assertEqual(encrypt_caesar("xyz", 2), "zab")
        self.assertEqual(encrypt_caesar("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_decrypt_default_shift(self):
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")
        self.assertEqual(decrypt_caesar(""), "")

    def test_decrypt_custom_shift(self):
        self.assertEqual(decrypt_caesar("BCD", 1), "ABC")
        self.assertEqual(decrypt_caesar("zab", 2), "xyz")
        self.assertEqual(decrypt_caesar("Mjqqt, Btwqi!", 5), "Hello, World!")