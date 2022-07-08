def one_swap_sorting(sequence):
    """
    list -> bool
    Return True if sequense is sorted after swapping two elements.
    False in other situations

    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    False
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """

    if len(sequence) < 2:
        return False
    if len(sequence) == 2 and sequence[0] == sequence[1]:
        return False
    wrong_position=0

    for i in range(1,len(sequence)):
        if sequence[i]<sequence[i-1]:
            wrong_position+=1
        if wrong_position > 2:
            return False

    if wrong_position == 0:
        return False

    return True

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())




