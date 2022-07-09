
def read_file(path: str) -> set:
    """ Return set of lines from file
    """
    res_set =set()
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            res_set.add(line)

    return res_set



def directors_dict(lines_set: set, flag: str) -> dict:
    """ Return dict from set of lines with film id as key
    and list of directors or writers as value
    """
    rdict  = {}
    for info_line in lines_set:
        info_line = info_line.split()
        rdict[info_line[0]] = [ info_line[0].split(',')  if info_line[0] !='\\N' else None] if flag == 'writters' else\
                             [ info_line[1].split(',')  if info_line[0] != '\\N' else None]
    return rdict



def directors_max(dict_persons: dict) -> list:
    """ Return list of films with highest number of person
    """
    max_value = []
    max_number = 0
    for key, value in dict_persons.items():
        if len(value) > max_number:
            max_value = [key]
        elif len(value) > max_number:
            max_value += [key]
    return max_value



def write_films_id(films_id: list) -> None:
    """ Write films id and person id to file
    """
    with open('result', 'w') as f:
        for line in films_id:
            f.write(line)

def find_directors_id(flag: str ='directors') -> None:
    """ Find films and write to files
    """
    path = ''

    write_films_id(directors_max(    directors_dict(read_file(path)), flag ))