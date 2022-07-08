"""
Module to find names that suits both for female and male
"""

def common_names(female_names, male_names):
    """
    Compare of two lists with people names
    Retrun set of words that are on both lists
    >>> common_names(['Mary', 'Gerry'], ['Sam', 'Gerry', 'Joe'])
    set()
    >>> common_names(['Anna', 'Ali', 'Olivia', 'Austin' ], ['Austin', 'John', 'Ali', 'Jack'])
    {'Austin', 'Ali'}
    """
    common_names_set = set(female_names) & set(male_names)
    result =set()
    for name in common_names_set:
        if name[0] in ['A','O','E','U','I']:
            result.add(name)
    return result


def names_read(file_name):
    """
    Read file and return list strings
    """
    with open(file_name,'r', encoding='utf-8') as file:
        list_of_filelines =[]
        for line in file:
            list_of_filelines.append(line.strip())
    return list_of_filelines

print(common_names(names_read('female.txt'), names_read('male.txt')))

import doctest
print(doctest.testmod())