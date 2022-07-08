import sys


def return_digits(number):
    """
    Return input number with digit symbols.
    >>> return_digits(1)
    ' 1 \\n11 \\n 1 \\n 1 \\n 1 \\n 1 \\n111'
    >>> return_digits(42)
    '   4   222 \\n  44  2   2\\n 4 4  2  2 \\n4  4    2  \\n444444 2   \\n   4  2    \\n   4  22222'
    """
    Zero = ["  ***  ",
            " *   * ",
            "*     *",
            "*     *",
            "*     *",
            " *   * ",
            "  ***  "]
    One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
    Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
    Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
    Four = ["   *  ", "  **  ", " * *  ",
            "*  *  ", "******", "   *  ", "   *  "]
    Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
    Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
    Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
    Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
    Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
    Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

    digits = str(number)
    row = 0
    line = ""
    while row < 7:
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for symbol in digit[row]:
                if symbol == '*':
                    line += f'{number}'
                else:
                    line += ' '
            column += 1
        line += '\n'
        row += 1
    return line[:-1]

if __name__ == '__main__':
    try:
        digits = sys.argv[1]
        print(return_digits(digits))
    except IndexError:
        print("usage: bigdigits.py <number>")
    except ValueError as err:
        print(err, "in", digits)

    import doctest
    print(doctest.testmod())
