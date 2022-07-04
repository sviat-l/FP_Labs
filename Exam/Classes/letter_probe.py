"""
Exam task 1.2 Letters Unittests
"""
import unittest
from letters import First, Second


class TestNumbers(unittest.TestCase):
    """
    Main class to test letters module
    """

    def test_constructior(self):
        """
        Test basic methods:
            __init__
            __str__
        """

        alpha1 = First('miraculously')  # First's constructor takes	variable of	arguments
        self.assertEqual(alpha1.consonants, ['m','r','c','l','s','l'])  # consonants are in the original order
        self.assertEqual(alpha1.vowels, ['i','a','u','o','u','y'])  # but vowels are in the original order
        self.assertEqual(str(First('miraculous')), "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=['i', 'a', 'u', 'o', 'u'])")

    def test_equal(self):
        """
        Check equal operator: __eq__
        """
        # Two First's are equal if their consonants are equal.
        self.assertEqual(First('myricyl'), First('miracle'))
        self.assertNotEqual(First('miraculously'), First('miraculous'))
        self.assertNotEqual(First('miraculously'), "don't	crash	here!")

        s = []
        self.assertNotIn(First('myricyl'), s)
        s.append(First('myricyl'))
        self.assertIn(First('myricyl'), s)
        self.assertIn(First('miracle'), s)


    def test_clear(self):
        """
        Test clear methods:
                clear_vowels
                cleared_vowels
        """
        # clear_vowels and cleared_vowels are different methods (one is	destructive)
        alpha2 = First('miraculous')
        alpha2.clear_vowels()
        self.assertEqual(str(alpha2), "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=[])")
        alpha3 = First('miraculous')
        alpha4 = alpha3.cleared_vowels()
        self.assertTrue(isinstance(alpha4, First))
        self.assertEqual(str(alpha3), "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=['i', 'a', 'u', 'o', 'u'])")
        self.assertEqual(str(alpha4), "First(consonants=['m', 'r', 'c', 'l', 's'], vowels=[])")

    def test_encoder(self):
        """
        Check Second class, and encoder method
        """
        beta1 = Second('miracle',5)  # creates	an First with 5 as shift
        self.assertTrue(isinstance(beta1, First))
        self.assertEqual(str(beta1), "First(consonants=['m', 'r', 'c', 'l'], vowels=['i', 'a', 'e'])") # use __class__, __bases__, __name__ attribute

        # only Second's object can call encoder:
        beta2 = beta1.encoder()  # so	instead	of 'miracle' it's now "rnwfhqj" by shift using
        self.assertEqual(str(beta2), "First(consonants=['r', 'w', 'h', 'q', 'n', 'f', 'j'], vowels=[])") # encoding consonants then vowels
        self.assertTrue(isinstance(beta2, Second))

        crashed = False
        try:
            alpha = First('abc').encoder()
        except:
            crashed = True
            self.assertTrue(crashed)

if __name__ ==  '__main__':
    unittest.main()
