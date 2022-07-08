def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('C', 'b')
    True
    >>> compare_char('d', 'ad')

    >>> compare_char('2', 2)

    """

    if type(ch1) != str or type(ch2) != str or len(ch1)*len(ch2) != 1:
        return None
              
    if 64 < ord(ch1) < 91:
        ch1 = chr((ord(ch1) + 32))
    if 64 < ord(ch2) < 91:
        ch2 = chr((ord(ch2) + 32))

    for i in [ch1, ch2]:
        if ord(i) > 122 or ord(i) < 97:
            return None

    if ord(ch1) > ord(ch2): 
        return True
    else:
        return False


print(compare_char('z', 2))

#done

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())