"""Sieve flavius sequenses"""

def sieve_flavius(number):
    """
    int -> list
    Arguments:
        number type = int
    Return list of lucky numbers  that are less than number
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(50)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(2)
    [1]
    >>> sieve_flavius(1)
    [1]
    >>> sieve_flavius(0)
    []
    """
    if number < 3 :
        return list(range(1,((number+3)//2)))
    lst = list(range(1,number,2))
    i = 1
    while True:
        current_number = lst[i]
        number_of_elements_to_delete = (len(lst) // current_number)
        if number_of_elements_to_delete > 0:
            index_to_delete =  number_of_elements_to_delete * current_number
        else:
            break
        while index_to_delete > 0:
            lst.pop( index_to_delete - 1)
            index_to_delete -= current_number
        i += 1
    return lst
