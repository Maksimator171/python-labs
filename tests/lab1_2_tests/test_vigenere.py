import unittest
from vigenere import encrypt_vigenere, decrypt_vigenere

class TestVigenere(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(encrypt_vigenere("Hello", "KEY"), "Rijvs")

    def test_decrypt(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")
        self.assertEqual(decrypt_vigenere("Rijvs", "KEY"), "Hello")