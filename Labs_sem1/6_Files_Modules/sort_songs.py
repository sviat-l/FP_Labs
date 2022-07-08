"""Sort songs module"""

def song_length(one_song_tuple) -> float:
    """
    tuple[str,float] -> float
    Got tuple with song name and its duration
    Return its duration
    >>> song_length(('November rain',9.17))
    9.17
    """
    return one_song_tuple[1]

def title_length(one_song_tuple) -> int:
    """
    tuple[str,float] -> int
    Got tuple with song name and its duration
    Return its name length
    >>> title_length(('November rain',9.17))
    13
    """
    return len(one_song_tuple[0])

def last_word(one_song_tuple) -> str:
    """
    tuple[str,float] -> str
    Got tuple with song name and its duration
    Return its last word in lower register
    >>> last_word(('November rain',9.17))
    'rain'
    >>> last_word(('Ride',3.34))
    'ride'
    """
    return one_song_tuple[0].split()[-1].lower()

def sort_songs(song_titles, length_songs, key):
    """
    (list, list, str) ->
    Return list of tuples of songs with its names and duration
    sorted by a key. If len of lists is not equal return None
    Parameters:
        song_titles = list of song titles
        length_songs - list of songs length
        key - key for sorting one of
    (song_length, title_length, last_word)
    Expectation:
        len(song_titles) == len(length_songs)
    >>> sort_songs(['Той день', 'Мало мені', 'Відпусти','Коли тебе нема'],\
                   ['3.58', '5.06','3.52','3.17'], song_length)
    [('Коли тебе нема', '3.17'), ('Відпусти', '3.52'), ('Той день', '3.58'), ('Мало мені', '5.06')]
    >>> sort_songs(['Той день', 'Мало мені', 'Відпусти','Коли тебе нема'],\
                   ['3.58', '5.06','3.52','3.17'], title_length)
    [('Той день', '3.58'), ('Відпусти', '3.52'), ('Мало мені', '5.06'), ('Коли тебе нема', '3.17')]
    >>> sort_songs(['Той день', 'Мало мені', 'Відпусти','Коли тебе нема'],\
                   ['3.58', '5.06','3.52','3.17'], last_word)
    [('Відпусти', '3.52'), ('Той день', '3.58'), ('Мало мені', '5.06'), ('Коли тебе нема', '3.17')]
    """
    if len(song_titles) != len(length_songs):
        return None
    not_sorted_list = []
    number_of_songs = len(length_songs)
    for i in range(number_of_songs):
        not_sorted_list.append((song_titles[i], length_songs[i]))
    return sorted(not_sorted_list, key=key)

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
