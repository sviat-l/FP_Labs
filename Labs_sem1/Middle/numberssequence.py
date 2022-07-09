"""
Middle task 1
Number sequence
"""

def number_sequence(length: int) -> list:
    """
    Return list of the first length elements from\n
    the sequence that is set by the special rules
    >>> number_sequence(6)
    [0, 0, 0, 0, 0, 24]
    >>> len(number_sequence(9))
    9
    >>> type(number_sequence(5)) == list
    True
    >>> number_sequence(15)
    [0, 0, 0, 0, 0, 24, 120, 0, 0, 19704, 0, 704912, 2200, 0, 117664]
    """
    result = []
    for n in range(1, length+1):
        k = 1
        while not is_palindrom(k*(2*n-1)):
            k += 1
        result.append( k ^ (k**3))
    return result


def is_palindrom(number:int) -> float:
    """
    Check if binary representation of the number is a palindrom.\n
    Return True if yes, otherwise False
    >>> is_palindrom(1)
    True
    >>> is_palindrom(20)
    False
    >>> is_palindrom(255)
    True
    >>> is_palindrom(1245)
    False
    """
    return bin(number)[2:] == bin(number)[2:][::-1]

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
