"""
Recurcive functions
"""
import cProfile
import pstats

def create_table(row_number, collumn_number):
    """
    (int, int) -> [list[list]]
    Return table with where every element is a sum of element uppon it and left from it
    If there is no left or no upper element its equel to 1
    row_number - number of rows  : expectation row_number > 0
    collumn_number - number of collumns : expectations collumn_number > 0
    create_table
    >>> create_table(1, 1)
    [[1]]
    >>> create_table(2, 2)
    [[1, 1], [1, 2]]
    >>> create_table(1, 6)
    [[1, 1, 1, 1, 1, 1]]
    >>> create_table(4, 6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    >>> create_table(6, 4)
    [[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 6, 10], [1, 4, 10, 20], [1, 5, 15, 35], [1, 6, 21, 56]]
    >>> create_table(6, 6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56], \
[1, 5, 15, 35, 70, 126], [1, 6, 21, 56, 126, 252]]
    """
    table = [[1] * collumn_number] if collumn_number > 0 else []
    for _ in range(row_number-1):
        table.append([1] + [0]*(collumn_number-1))

    def table_element(i, j):
        if i > -1 and j > -1:
            if  not table[i-1][j]:
                table_element(i-1, j)
            if  not table[i][j - 1]:
                table_element(i, j - 1)
            table[i][j] = table[i-1][j] + table[i][j-1]
    if not table[row_number-1][collumn_number -1]:
        table_element(row_number-1, collumn_number -1 )
    return table

print(create_table(5, 5))


def flatten(starting_list):
    """
    list -> list
    >>> flatten(1)
    1
    >>> flatten([])
    []
    >>> flatten([[[]], [5]])
    [5]
    >>> flatten([[True],[1,2],[],4536,[['fdb'],['bdfgb', 5]],[['123']]])
    [True, 1, 2, 4536, 'fdb', 'bdfgb', 5, '123']
    >>> flatten([[[[[[]]]]]])
    []
    """
    if  not isinstance(starting_list, list):
        return starting_list
    if  not starting_list:
        return []
    number_ofelements = len(starting_list)
    for _ in range(number_ofelements):
        if not isinstance(starting_list[0], list):
            starting_list.append(starting_list[0])
        else:
            starting_list.extend(flatten(starting_list[0]))
        starting_list.pop(0)
    return starting_list

if __name__ == '__main__':
#     row_num, collumn_num = input().split()
#     result_table = create_table(int(row_num), int(collumn_num))
#     space_for_numbers = int(len(str(result_table[-1][-1])) + 2)
#     space_for_numbers = 5
#     for row in result_table:
#         output = ''
#         for cur_number in row:
#             output += f'{cur_number:{space_for_numbers}}'
#         print(output)
# import doctest
# print(doctest.testmod())

    with cProfile.Profile() as pf:
        create_table(200, 200)
        stats = pstats.Stats(pf)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
