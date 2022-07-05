"""
MODULE to work with kved.json
"""
import json


def parse_kved(class_code: str) -> None:
    """
    main function read object from json_file, find nesessery parametrs and write results
    """
    data = get_information('kved.json')['sections'][0]

    # get section name and it children number
    section_index = binary_search_section(data, class_code[:2], 0, len(data))
    section_name = data[section_index]['sectionName']
    data = data[section_index]['divisions']
    section_number = len(data)

    # get division name and it children number
    division_index = binary_search(
        data, 'divisionCode', class_code[:2], 0, len(data))
    division_name = data[division_index]['divisionName']
    data = data[division_index]['groups']
    division_number = len(data)

    # get group name and it children number
    group_index = binary_search(
        data, 'groupCode', class_code[:4], 0, len(data))
    group_name = data[group_index]['groupName']
    data = data[group_index]['classes']
    group_number = len(data)

    # get class name
    class_index = binary_search(data, 'classCode', class_code, 0, len(data))
    class_name = data[class_index]['className']

    # write data in a file
    json_object = {"name": class_name,  "type": "class", "parent": {
        "name": group_name, "type": "group", "num_children": group_number, "parent": {
            "name": division_name, "type": "division", "num_children": division_number, "parent": {
                "name": section_name, "type": "section", "num_children": section_number
            }}}}
    write_data(json_object, 'kved_results.json')


def binary_search_section(data: dict, flag: str, left: int, right: int) -> int:
    """
    find index of element that contains a dictionary with value equel to flag
    >>> binary_search_section([\
        { "sectionCode": "A",  "sectionName": '2 Course',\
    "divisions": [{ "divisionCode": "01", 'name':'OOP'}, { "divisionCode": "02", 'name':'C++'}]},\
        { "sectionCode": "B",  "sectionName": '1 Course',\
    "divisions": [{ "divisionCode": "03", 'name':'OP'}, { "divisionCode": "04", 'name':'Python'}]}\
                            ], '01', 0, 2)
    0
    >>> binary_search_section([\
        { "sectionCode": "A",  "sectionName": '2 Course',\
    "divisions": [{ "divisionCode": "01", 'name':'OOP'}, { "divisionCode": "02", 'name':'C++'}]},\
        { "sectionCode": "B",  "sectionName": '1 Course',\
    "divisions": [{ "divisionCode": "03", 'name':'OP'}, { "divisionCode": "04", 'name':'Python'}]}\
                            ], '04', 0, 2)
    1
    """
    mid = (left + right)//2
    if data[mid]['divisions'][0]['divisionCode'] > flag:
        return binary_search_section(data, flag, left, mid-1)
    elif data[mid]['divisions'][-1]['divisionCode'] < flag:
        return binary_search_section(data, flag, mid+1, right)
    return mid


def binary_search(data: dict, key: str, flag: str, left: int, right: int):
    """
    find index of element that contains a dictionary with value equel to flag
    >>> binary_search(\
        [{ "divisionCode": "01", 'name':'OOP'}, { "divisionCode": "02", 'name':'C++'},\
        { "divisionCode": "03", 'name':'OP'}, { "divisionCode": "04", 'name':'Python'}],\
            'divisionCode', '02', 0, 3)
    1
    >>> binary_search(\
        [{ "divisionCode": "01", 'name':'OOP'},\
        { "divisionCode": "03", 'name':'OP'}, { "divisionCode": "04", 'name':'Python'}],\
            'divisionCode', '03', 0, 3)
    1
    >>> binary_search(\
        [{ "divisionCode": "01", 'name':'OOP'}, { "divisionCode": "02", 'name':'C++'},\
        { "divisionCode": "03", 'name':'OP'}, { "divisionCode": "04", 'name':'Python'}],\
            'divisionCode', '04', 0, 3)
    3
    """
    mid = (left + right)//2
    if data[mid][key] > flag:
        return binary_search(data, key, flag, left, mid-1)
    if data[mid][key] < flag:
        return binary_search(data, key, flag, mid+1, right)
    return mid


def get_information(path: str):
    """
    read and return data from the json file on the path
    """
    with open(path, 'r', encoding='utf-8') as open_file:
        data = json.load(open_file)
    return data


def write_data(json_object: dict, file_path: str):
    """
    write data into a json file on a path
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_object, file,  ensure_ascii=False, indent=4)
