def convert_to_column(s):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> convert_to_column("Revenge is a dish that tastes best when served cold.")
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> convert_to_column("Never hate your enemies. It affects your judgment.")
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> convert_to_column(2015)
    """

    if not isinstance(s, str):
        return None

    list_of_text = s.split()
    output = []
    i = 0

    for word in list_of_text:
        if word!=' ':
            output.append('')
            for symbol in word:
                if 64 < ord(symbol) < 91:
                    output[i] += symbol.lower()
                elif 96 < ord(symbol) < 123:
                    output[i] += symbol
        i += 1

    return print( '\n'.join(output))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())