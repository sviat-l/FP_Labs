"""
Lab 7.5 Tests Vinegere Cipher
"""

import unittest
from vigenere_cipher import VigenereCipher, combine_character, separate_character

class TestVinegereCipher(unittest.TestCase):
    """ Class to run tests on vinegere cipher module """

    def test_extend_keyword(self):
        """
        Test extend keyword  class method
        """
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        assert extended == "TRAINTRAINTRAINT"

    def test_encode(self):
        """
        Test Vingere basic cases encode method
        """
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_character(self):
        """
        Test vinigere correct one character encoding
        """
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        assert encoded == "X"

    def test_encode_spaces(self):
        """
        Test vinegere correct space encoding
        """
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_lowercase(self):
        """
        Test vinegere correct lowercase encoding
        """
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_combine_character(self):
        """
        Test combine character funtion
        """
        assert combine_character("E", "T") == "X"
        assert combine_character("N", "R") == "E"

    def test_separate_character(self):
        """
        Test separating character function
        """
        assert separate_character("X", "T") == "E"
        assert separate_character("E", "R") == "N"

    def test_decode(self):
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        assert decoded == "ENCODEDINPYTHON"

if __name__ == '__main__':
    unittest.main()
