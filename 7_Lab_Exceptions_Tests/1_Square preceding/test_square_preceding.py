"""
Lab 7.1 Tests
Test square preceding
"""

import unittest
from square_preceding import square_preceding


class TestSquare(unittest.TestCase):
    """ Class to test module functions """

    def test_square_preceding(self):
        """ Run tests"""

        test_case = [1,2,3]
        square_preceding(test_case)
        self.assertEqual(test_case, [0,1,4])

        test_case = []
        square_preceding(test_case)
        self.assertEqual(test_case, [])

        test_case = [1, 2, 3, 2, 1]
        square_preceding(test_case)
        self.assertNotEqual(test_case, [0, 1, 4, 9, 16])


if __name__ == "__main__":
    unittest.main()
