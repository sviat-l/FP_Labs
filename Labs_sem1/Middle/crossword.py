"""
Middle task 2
Crossword
"""


def read_crossword(path: str) -> list:
    """
    Read file and get letters with their coordinates
    for crossword. Save them in the list with tuples
    in format (letter, (row, collumn))
    >>> result = read_crossword('crossword_3_2.txt')
    >>> type(result) == list
    True
    >>> type(result[0]) == tuple
    True
    >>> len(result)
    35
    """
    result = []
    with open(path, 'r', encoding='utf-8') as read_file:
        letter = ''
        for line in read_file:
            if not letter:
                letter = line.strip()
            else:
                for i in range(len(line)//2):
                    result.append((letter, (int(line[2*i]), int(line[2*i+1]))))
                letter = ''
    return result


def crossword_words(crossword: list[tuple]) -> list[str]:
    """
    Return list with the shortest words
    for the horisontal orientation
    >>> crossword = [('h', (1, 1)), ('e', (1, 2)), ('l', (1, 3)), ('l', (1, 4)), ('o', (1, 5))]
    >>> result = crossword_words(crossword)
    >>> type(result) == list
    True
    >>> len(result)
    1
    >>> result
    ['hello']
    """
    board_crossword = [[' ' for _ in range(8)] for _ in range(8)]
    # restore crossword as 2D array
    for letter, (i, j) in crossword:
        board_crossword[i][j] = letter
    # get all horisontal words with len >= 3
    words = [word for crossword_row in board_crossword
             for word in ''.join(crossword_row).split() if len(word) > 2]
    min_length = len(min(words, key=len))
    return [word for word in words if len(word) == min_length]


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    crossword = read_crossword('crossword_3_2.txt')
    if crossword_words(crossword) == ['soon', 'sump']:
        print('Wrong result')
