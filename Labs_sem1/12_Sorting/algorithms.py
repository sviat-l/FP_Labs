""" Search and sort algoritms """


def linear_search(list_of_values, value):
    """
    (list, ) -> int
    return index of the element in the list, if it is not in the list return -1\
    done by linear search
    >>> linear_search([1, 4, 423, 23, 2, 3, 65], 65)
    6
    >>> linear_search([1, 4, 423, 23, 2, 3, 65], 0)
    -1
    >>> linear_search(['ahf', 'bdf', 'ssd', 'csdg', 'ddsfg'], 'ssd')
    2
    >>> linear_search([['ahf'], ['bdf'], ['ssd', 'csdg'], ['ddsfg']], 'ssd')
    -1
    """
    for i, cur_value in enumerate(list_of_values):
        if cur_value == value:
            return i
    return -1


def merge_sort(lst:list) -> list:
    """
    Return sorted list with variables
    done by merge sorting
    >>> merge_sort([2, 7, 52, 42, 11, 513, 35, 4, 53, 22])
    [2, 4, 7, 11, 22, 35, 42, 52, 53, 513]
    >>> merge_sort([])
    []
    >>> merge_sort([1])
    [1]
    >>> merge_sort([2,5,0])
    [0, 2, 5]
    >>> merge_sort([4, 513, 7, 35, 2, 64, 22, 1, 42, 11])
    [1, 2, 4, 7, 11, 22, 35, 42, 64, 513]
    >>> merge_sort([5, 7])
    [5, 7]
    """
    if len(lst) < 2:
        return lst
    left,right, lst = merge_sort(lst[:(len(lst) + 1)//2]), merge_sort(lst[(len(lst) + 1) //2:]), []
    while True:
        if not left:
            return lst + right
        if not right:
            return lst + left
        if left[0] > right[0]:
            lst.append(right.pop(0))
        else:
            lst.append(left.pop(0))


def binary_search(list_of_values, value):
    """
    (list, int) -> int
    return index of the element in the list, if it is not in the list return -1\
    done by linear search
    >>> binary_search([1, 2, 4, 7, 11, 15, 42, 52, 53, 513], 53)
    8
    >>> binary_search([1, 2, 4, 7, 11, 15, 22, 35, 42, 52, 53, 63, 64, 513], 22)
    6
    >>> binary_search([1, 2, 4, 7, 11, 15, 22, 35, 42, 52, 53, 63, 64, 513], 513)
    13
    """
    left_index, right_index = 0, len(list_of_values) - 1
    while left_index <=  right_index:
        middle_index = (right_index + left_index)//2
        if list_of_values[middle_index] == value:
            return middle_index
        elif list_of_values[middle_index] > value:
            right_index = middle_index -1
        else:
            left_index = middle_index + 1
    return -1

def selection_sort(lst:list) -> list:
    """
    return sorted list with values
    >>> selection_sort([2, 7, 52, 42, 11, 513, 35, 4, 53, 22])
    [2, 4, 7, 11, 22, 35, 42, 52, 53, 513]
    >>> selection_sort([])
    []
    >>> selection_sort([1])
    [1]
    >>> selection_sort([2,5,0])
    [0, 2, 5]
    >>> selection_sort([4, 513, 7, 35, 2, 64, 22, 1, 42, 11])
    [1, 2, 4, 7, 11, 22, 35, 42, 64, 513]
    >>> selection_sort([5, 7])
    [5, 7]
    """
    for i, value in enumerate(lst):
        current_min = i
        for j in range(i + 1, len(lst)):
            if lst[current_min] > lst[j]:
                current_min = j
        lst[current_min], lst[i] = value, lst[current_min]
    return lst

def quick_sort(lst:list) -> list:
    """
    return sorted list with values
    >>> quick_sort([2, 7, 52, 42, 11, 513, 35, 4, 53, 22])
    [2, 4, 7, 11, 22, 35, 42, 52, 53, 513]
    >>> quick_sort([])
    []
    >>> quick_sort([1])
    [1]
    >>> quick_sort([2,5,0])
    [0, 2, 5]
    >>> quick_sort([4, 513, 7, 35, 2, 64, 22, 1, 42, 11])
    [1, 2, 4, 7, 11, 22, 35, 42, 64, 513]
    >>> quick_sort([5, 7])
    [5, 7]
    """
    return lst if len(lst) < 2 else quick_sort([lst.pop(i) for i in range(len(lst)-1,0,-1) if  lst[i] < lst[0]]) + [lst.pop(0)] + quick_sort(lst)

    return lst if len(lst) < 2 else quick_sort([lst[i] for i in range(len(lst)-1,0,-1)\
                                            if  lst[i] < lst[0]]) + [lst[0]] + quick_sort(lst)



# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())
