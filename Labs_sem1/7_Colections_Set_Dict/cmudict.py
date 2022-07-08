"""
Work with prononciation dictionaries
"""
from time import time
start = time()


def dict_reader_tuple(file_dict):
    """
    str -> tuple[str,int,list]
    Read file return tuple with word its number, and  current prononciation
    e.g  ("NACHOS", 2, ["N", "AE1", "CH", "OW0", "Z"]).
    """
    pronunciation_list = []
    with open(file_dict, 'r', encoding='utf-8') as file:
        for word in file:
            word = word.strip().split()
            pronunciation_list.append((word[0], int(word[1]), list(word[2:])))
    return pronunciation_list

# print(dict_reader_tuple('file_dict'))


def dict_reader_dict(file_dict):
    """
    str -> dict[str:set[tuples]]
    Read file return dict with words as a key and sets of all their prononciations
    e.g  {"NACHOS": set(("N", "AE1", "CH", "OW0", "Z"), ("N", "AA1", "CH", "OW0", "Z")), ....}
    """
    pronunciation_dict = {}
    with open(file_dict, 'r', encoding='utf-8') as file:
        for word in file:
            word = word.strip().split()
            if word[0] not in pronunciation_dict:
                pronunciation_dict[word[0]] = set()
            pronunciation_dict[word[0]].add(tuple(word[2:]))
    return pronunciation_dict

# print(dict_readers_dict('file_dict'))


def dict_invert(pron_dic):
    """
    tuple/dict -> dict[int:set[tuples[str, tuple]]]
    invert dictionary in format of dictionary or tuple into sorted by keys dictionaty
    key = number of pronounciations, value  -  words and therir possoble prononciations
    which number of prononciations is equal to key
    >>> dict_invert({'A.': {('EY1',)}})
    {1: {('A.', ('EY1',))}}
    >>> dict_invert([('A.', 1,  ['EY1',])])
    {1: {('A.', ('EY1',))}}
    >>> dict_invert([('A.', 1, ['EY1']), ('NACHOS', 1, ['N', 'AA1', 'CH', 'OW0', 'Z']),\
                                           ('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z'])]) ==\
        dict_invert({'A.': {('EY1',)}, 'NACHOS': {('N', 'AE1', 'CH', 'OW0', 'Z'),\
                                                  ('N', 'AA1', 'CH', 'OW0', 'Z')}})
    True
    """
    not_sorted_inverted_dict = {}
    if isinstance(pron_dic, dict):
        for word, word_prons in pron_dic.items():
            if len(word_prons) not in not_sorted_inverted_dict:
                not_sorted_inverted_dict[len(word_prons)] = set()
            for current_pronon in word_prons:
                not_sorted_inverted_dict[len(word_prons)].add(
                    (word, current_pronon))

    elif isinstance(pron_dic, list):
        while len(pron_dic) > 0:
            index_in_list = -1
            word, number_of_prons, pronons_list = pron_dic.pop()
            pronons_list = [pronons_list]
            while len(pronons_list) < number_of_prons:
                if word == pron_dic[index_in_list][0]:
                    pronons_list.append(pron_dic.pop(index_in_list)[-1])
                else:
                    index_in_list -= 1

            if number_of_prons not in not_sorted_inverted_dict:
                not_sorted_inverted_dict[number_of_prons] = set()
            for current_pronon in pronons_list:
                not_sorted_inverted_dict[number_of_prons].add(
                    (word, tuple(current_pronon)))

    inverted_dict = {}
    for key in sorted(not_sorted_inverted_dict):
        inverted_dict[key] = not_sorted_inverted_dict[key]
    return inverted_dict

# print(dict_reader_dict('file_dict'))
# print(dict_reader_tuple('file_dict'))

# print(dict_invert(dict_reader_dict('file_dict')))
# print(dict_invert(dict_reader_tuple('file_dict')))

# print(dict_invert(dict_reader_dict('cmudict')) == dict_invert(dict_reader_tuple('cmudict')))
# print(round((time() - start), 2))


# if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
