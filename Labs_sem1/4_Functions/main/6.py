def remove_spaces(s):
    """
    str -> str
    Remove all additional spaces in string and return a new string without additional spaces.
    If argument is not a string function should return None.

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    "I'll make him an offer he can't refuse."
    >>> remove_spaces("Great    men     are    not born great, they grow great...")
    'Great men are not born great, they grow great...'
    >>> remove_spaces("     No    matter    how hard  you tried...     ")
    'No matter how hard you tried...'
    >>> remove_spaces("    ")

    >>> remove_spaces("")

    >>> remove_spaces(2015)

    """
    
    if type(s) != str  or s==' '*len(s) :
        return None

    output=''
    starting=0
    finish=len(s)-1

    while s[starting]==' ':
        starting+=1

    while s[finish]==' ':
        finish-=1

    for i in range(starting, finish+1):
        if  not s[i]==s[i-1]==' ':
            output+=s[i]
            
    return output

print(remove_spaces("")) 

#done

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())