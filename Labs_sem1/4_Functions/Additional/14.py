def get_letters(n):
    """
    int -> str
    Create and return string of first n letters of an alphabet. If arguments isn't
    positive integer number function should return None.

    >>> get_letters(0)

    >>> get_letters(1)
    a
    >>> get_letters(20)
    abcdefghijklmnopqrst
    >>> get_letters(-2015)

    """
    if not isinstance(n,int) or n<1:
        return None
    output=''
    if n > 26: n=26
    for i in range(n):
        output+=chr(97+i)

    return output

print(get_letters(20))

#done
#n>26