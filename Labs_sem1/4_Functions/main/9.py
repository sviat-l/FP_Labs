def replace_with_stars(s):
    """
    str -> str
    Replace symbols in string with stars. If argument is not a string function should
    return None.

    >>> replace_with_stars("Revenge is a dish that tastes best when served cold.")
    '****************************************************'
    >>> replace_with_stars("Never hate your enemies. It affects your judgment.")
    '**************************************************'
    >>> replace_with_stars('  ')
    '**'
    >>> replace_with_stars('')
    
    >>> replace_with_stars('2015')   
    '****'
    >>> replace_with_stars(2015)

    """

    if type(s) != str or len(s)==0: return None
    return '*'*len(s)

print(replace_with_stars('  '))

#done

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())