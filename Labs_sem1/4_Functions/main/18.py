def number_of_capital_letters(s):
    """
    str -> str
    Find and return number of capital letters in string. If argument isn't string
    function should return None.

    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_capital_letters("EOFError")
    4
    >>> number_of_capital_letters("WHAT IS IT")
    8
    >>> number_of_capital_letters("error")
    0
    >>> number_of_capital_letters(1)

    """
    number=0
    if type(s) != str:
        return None
    
    for symbol in s:
        if 91>ord(symbol)>64:
            number+=1
    return number

print(number_of_capital_letters('error'))
#done
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())