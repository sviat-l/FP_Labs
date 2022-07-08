def compare_str(s1, s2):
    """
    (str, str) -> bool
    Compare two srings lexicographicly. Return True if string s1 is larger
    than string s2 and False otherwise. If arguments aren't string or function
    have different length function should return None.

    >>> compare_str('abc', 'Abd')
    False
    >>> compare_str('zaD', 'zab')
    True
    >>> compare_str('zaD', 'Zad')
    False
    >>> compare_str('AAbCHIfGlWeNNrsFHxyZ', 'ABDfgOlkHTrSpKlQQzXY')
    False
    >>> compare_str('aaa', 'aaaaa')

    >>> compare_str('2015', 2015)

    """
    lex1=lex2=0
    if not isinstance(s1,str) or not  isinstance(s2,str) or not len(s1)==len(s2):
         return None

    for symbol1 in s1:
        if 64<ord(symbol1)<91:
            lex1+=ord(symbol1)+ 32
        elif 96<ord(symbol1)<123:
            lex1+=ord(symbol1)
        else: return None

    for symbol2 in s2:
            if 64<ord(symbol2)<91:
                lex2+=ord(symbol2)+ 32
            elif 96<ord(symbol2)<123:
                lex2+=ord(symbol2)
            else: return None
            
    if lex1>lex2:
        return True
    else: return False
    
   

print(compare_str('AAbCHIfGlWeNNrsFHxyZ', 'ABDfgOlkHTrSpKlQQzXY'))
#done