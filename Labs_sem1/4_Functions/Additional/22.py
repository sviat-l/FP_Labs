def pattern_number(sequence):
    """
    >>> pattern_number([])
    None
    >>> pattern_number([42])
    None
    >>> pattern_number([1,2])
    None
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    None
    >>> pattern_number([1,2,3,1,2,3])
    ([1,2,3], 2)
    >>> pattern_number([1,2,3,1,2])
    None
    >>> pattern_number([1,2,3,1,2,3,1])
    None
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    None
    """
    pattern=''
    sequence_str=''
    for symbol in sequence:
        sequence_str+=str(symbol)

    for i in range(len(sequence)//2 +1):
        pattern+=str(sequence_str[i])
        if len(sequence) % len(pattern)==0:
            number=int(len(sequence) / len(pattern))
            if sequence_str.count(pattern) == number :
                if type(sequence)==str:
                    return (pattern, number)
                else:
                    pattern=[int(x) for x in pattern]
                    return (pattern, number)
    return None

print(pattern_number([1,2,1,2,1,2]))
#done   not optimized