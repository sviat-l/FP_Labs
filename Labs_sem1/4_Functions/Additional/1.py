def get_position(ch):
    """
    str -> int
    Return positon of letter in alphabet. If argument is not a letter function
    should return None.

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')

    >>> get_position(2015)

    """
    if isinstance(ch, str) and len(ch)==1:
        if 64<ord(ch)<91:
            return ( ord(ch) - 64)
        if 96<ord(ch)<123:
            return ( ord(ch) - 96)
    return None

print(get_position('z'))
#done