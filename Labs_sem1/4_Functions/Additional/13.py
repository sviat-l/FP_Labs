def create_string(lst):
    """
    list -> str
    Create and return string from histogrma of letters. If argument isn't list of 26 positive
    integer numbers function should return None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    bcc
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4])
    aaaazzzz
    >>> create_string([4, 1, 2, 0, 1, 4, 0, 2, 0, 1, 0, 3, 0, 2, 1, 0, 4, 2, 0, 0, 2, 0, 3, 0, 2, 2])
    aaaabcceffffhhjlllnnoqqqqrruuwwwyyzz
    >>> create_string([4, 0, 0, 0, 0, 0])

    """
    if  not isinstance(lst, list) or  not len(lst)==26 :
        return None
    
    output=''

    for i in range(26):
        output+= chr(97+i)*lst[i]

    return output

x=[4, 1, 2, 0, 1, 4, 0, 2, 0, 1, 0, 3, 0, 2, 1, 0, 4, 2, 0, 0, 2, 0, 3, 0, 2, 2]

print(create_string(x))
#done