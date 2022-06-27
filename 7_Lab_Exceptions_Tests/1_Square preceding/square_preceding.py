"""
Lab 7.1 Square Preceding
"""

def square_preceding(values):
    """ (list of number) -> NoneType

    Replace each item in the list with square the value of the
    preceding item and replace the first item with 0.

    >>> L = [1, 2, 3]
    >>> square_preceding(L)
    >>> L
    [0, 1, 4]
    """
    if values != []:
        temp = 0
    for i, value in enumerate(values):
        values[i] = temp**2
        temp = value


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
