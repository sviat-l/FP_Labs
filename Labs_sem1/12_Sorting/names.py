"""
Work with children names base
"""

def find_names(file_path):
    """
    return tuple with inpormation about most popular name
    :First element: set with name of 3 most frequent names
    :Second element: tuple with number of names that are only one time  and set with their names
    :Third element: tuple with letter, number of names, and number of people with that names
    """
    top_3_list = [('', 0),('', 0),('', 0)]
    one_person_name_set = set()
    dict_names_by_letters = {}
    # list_with_names = []

    with open(file_path, 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            name, number = line.split()
            number = int(number[1:-1])
            # list_with_names.append((name, number))

            if number == 1:
                one_person_name_set.add(name)

            dict_names_by_letters[name[0]] = [dict_names_by_letters.get(name[0], [0, 0])[0] + 1,\
                                             dict_names_by_letters.get(name[0], [0, 0])[1] + number]

            position = 0
            while position < 3 and top_3_list[position][1] < number :
                position += 1
            top_3_list.insert(position,(name, number))
            top_3_list = top_3_list[1:]


    first_result = set([x[0] for x in top_3_list])
    second_result = (len(one_person_name_set), one_person_name_set)
    third_result = max_of_dict(dict_names_by_letters)
    # max_number = 0
    # for key, value in dict_names_by_letters.items():
    #     if value[0] > max_number:
    #         third_result, max_number = (key, value[0], value[1]), value[0]

    return first_result, second_result, third_result



def max_of_dict(dict_names_by_letters):
    """
    dict -> tuple[str, int, int]
    Return tuple with info about
    >>> max_of_dict({'А': [55, 1752], 'Б': [8, 79], 'В': [21, 1291], 'Г': [9, 33], 'Ґ': [2, 2],\
    'Д': [20, 642], 'Е': [27, 326], 'Є': [16, 455], 'Ж': [2, 4], 'З': [6, 391], 'І':[19, 278],\
    'Й': [4, 4], 'К': [17, 410], 'Л': [31, 144], 'М': [41, 1171], 'Н': [17, 163], 'О': [13, 408],\
    'П': [7, 85], 'Р': [19, 98], 'С': [17, 1225], 'Т': [9, 176], 'У': [2, 70], 'Ф': [4, 4],\
     'Х': [9, 206], 'Ц': [1, 1], 'Ш': [1, 1], 'Ю': [10, 393], 'Я': [11, 513]})
    ('А', 55, 1752)
    >>> max_of_dict({'А': [41, 1065], 'Б': [7, 286], 'В': [21, 858], 'Г': [9, 38], 'Ґ': [1, 1],\
 'Д': [32, 1689], 'Е': [11, 23], 'Є': [6, 56], 'Ж': [1, 1], 'З': [8, 192], 'І': [12, 410],\
 'Й': [5, 13], 'К': [13, 93], 'Л': [18, 241], 'М': [30, 2510], 'Н': [13, 339], 'О': [12, 968],\
 'П': [6, 245], 'Р': [13, 379], 'С': [23, 478], 'Т': [14, 375], 'У': [2, 80], 'Ф': [5, 6],\
 'Х': [2, 2], 'Ш': [1, 1], 'Ю': [5, 338], 'Я': [8, 190]})
    ('А', 41, 1065)
    """
    max_number = 0
    for key, value in dict_names_by_letters.items():
        if value[0] > max_number:
            result, max_number = (key, value[0], value[1]), value[0]
    return result
print(find_names('girl_names'))