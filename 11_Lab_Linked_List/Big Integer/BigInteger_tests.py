"""
Tests for BigInteger class
"""
import unittest

from big_integer import BigInteger


class TestValidator(unittest.TestCase):

    def test_general(self):
        """
        General tests. Init, str
        """
        for number in [1, 0, -151, 15, 143251212612461437542576354273, -3251, 6365437]:
            assert(str(BigInteger(str(number))) == str(number)), number
            assert(len(BigInteger(str(number))) ==
                   len(str(abs(number)))), number

        print('GENERAL TESTS PASSED SUCCESSFULLY\n')

    def test_comparable(self):
        """
        Test comparing operators: >, < ==, ...
        """
        for i in [12, -56, 234, -3939144]:
            for j in [59, 2, -15, -3939145]:
                x = BigInteger(str(i))
                y = BigInteger(str(j))
                assert((i > j) == (x > y)), (i, j, i > j, x > y)
                assert((i < j) == (x < y)), (i, j, i < j, x < y)
                assert((i <= j) == (x <= y)), (i, j, i <= j, x <= y)
                assert((i >= j) == (x >= y)), (i, j, i >= j, x >= y)
                assert((i == j) == (x == y)), (i, j, i == j, x == y)
                assert((i != j) == (x != y)), (i, j, i != j, x != y)
        print("COMPARABLE TESTS PASSED SUCCESSFULLY\n")

    def test_arithmetic(self):
        """
        Test arithmetic part:
            Adding
            Substraction
            Multiplication
            Power
            Modulo
            Floor division
            Divmod
        """
        # ADDING
        for i in [12, -76, 234, -2493939]:
            for j in [59, 2, -15, -144051]:
                x = BigInteger(str(i))
                y = BigInteger(str(j))
                assert(i+j == int(str(x+y))), (i, j, i+j, x+y)
        # print('Adding tests passed')

        # SUBSTRACTION
        for i in [-31, 12, -100001, 9099090]:
            for j in [-1, 0, 2, -10090, 9]:
                x = BigInteger(str(i))
                y = BigInteger(str(j))
                assert(i-j == int(str(x-y))), (i, j, i-j, x-y)
        # print('Substraction tests passed')

        # MULTIPLICATION
        for i in [-31, 1, 234, 623634]:
            for j in [-1, 1, 0, 2, 15, 515215]:
                x = BigInteger(str(i))
                y = BigInteger(str(j))
                assert(i*j == int(str(x*y))), (i, j, i*j, x*y)
        # print('Multiplication tests passed')

        # POWER
        for i in [0, 1, -3, 11, 25]:
            for j in [0, 1, 2, 5, 12, 31]:
                x = BigInteger(str(i))
                y = BigInteger(str(j))
                assert(i**j == int(str(x**y))), (i, j, i**j, x**y)
        # print('Power tests passed')

        # FLOOR DIVISION
        for i in [3, -3, -5, 5, 1345, -1345, 16, -16]:
            for j in [-2, 2, 12, -4, 4 - 12, 1, -1]:
                x = BigInteger(str(i))
                y = BigInteger(str(j))
                assert(i//j == int(str(x//y))), (i, j, i//j, x//y)
        # print('Floor division tests passed')

        # MODUL
        for i in [3, -3, -5, 5, 1345, -1345, 16, -16]:
            for j in [-3, 3, 12, -12]:
                x = BigInteger(str(i))
                y = BigInteger(str(j))
                assert(i % j == int(str(x % y))), (i, j, i % j, x % y)
        # print('Modular tests passed')

        # DIVMOD
        for i in [3, -3, -5, 5, 1345, -1345, 16, -16]:
            for j in [-4, 4]:
                x = BigInteger(str(i))
                y = BigInteger(str(j))
                assert(list(divmod(i, j)) == [int(str(n)) for n in x.big_divmod(y)]),\
                    (i, j, divmod(i, j), x.big_divmod(y))
        # print('Divmod tests passed')

        print('ARITHMETIC TESTS PASSED SUCCESSFULLY\n')

    def test_bitwise(self):
        """
        Test bitwise operators and functions:
                Into_bin
                Bin into integer
                Right/ Legt shift
                Bitwise AND, OR, XOR
        """

        # BIN TRANSFORMATION
        for i in [1, 2, 6, 11, 17, 63, 98]:
            x = BigInteger(str(i))
            assert(x.into_bin() == BigInteger(str(bin(i)[2:]))), x
            assert(x.into_bin().bin_into_integer() == x), x
        # print('Bin transforamtion passed')

        # RSHIF & LSHIFT
        for i in [1, 2, 6, 11, 17, 63, 98]:
            x = BigInteger(str(i))
            assert((x << BigInteger('1')) << BigInteger(
                '1') == x << BigInteger('2')), x
            assert((x << BigInteger('2')) << BigInteger(
                '3') == x << BigInteger('5')), x
        for i in [6, 11, 17, 63, 98]:
            x = BigInteger(str(i))
            assert((x >> BigInteger('1')) >> BigInteger(
                '1') == x >> BigInteger('2')), x
            assert((x << BigInteger('11')) >> BigInteger('11') == x), x
        # print('lshift & rshift passed')

        # BITWISE AND
        for i in [2, 5, 15, 63]:
            x = BigInteger(str(i))
            for j in [1, 2, 12, 17, 56]:
                y = BigInteger(str(j))
                assert (int(str(x & y)) == i & j), ((i, j), [x & y], i & j)
        # BITWISE OR
        for i in [2, 5, 15, 63]:
            x = BigInteger(str(i))
            for j in [1, 2, 12, 17, 56]:
                y = BigInteger(str(j))
                assert (int(str(x | y)) == i | j), ((i, j), [x | y], i | j)
        # BITWISE XOR
        for i in [2, 5, 15, 63]:
            x = BigInteger(str(i))
            for j in [1, 2, 12, 17, 56]:
                y = BigInteger(str(j))
                assert (int(str(x ^ y)) == i ^ j), ((i, j), [x ^ y], i ^ j)
        # print('Bitwise AMD, OR, XOR passed')

        print('BITWISE PART PASSED SUCCESSFULLY\n')



if __name__ == '__main__':
    unittest.main()
