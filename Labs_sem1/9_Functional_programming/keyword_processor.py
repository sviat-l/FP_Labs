"""
IMDB base
"""


def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    """
    Return set with key words that fits to the film fwith name film_name
    Arguments:
    :film_keywords - dictionary where key is a keyword and\
    value is a list with film names that have that key word
    :film_name - string with the name of the film
    >>> find_film_keywords( {'20-th century' : ['The Gift (2005/I) (V)', 'The Glass House (2009)',\
        'The Hip Hop Hoax (2013)', 'The Hitchcock of HipHop (2008) (V)', 'The Label (2007) (V)'],\
        'classic' : ['Le divin enfant (2001) (TV)', 'Le feu follet (1963)',\
        'Le salaire de la peur (1953)', 'Lord Jim (1965)', 'Love and Death (1975)',\
        'Lulu on the Bridge (1998)', "M'Liss (1936)", 'Maps to the Stars (2014)',\
        'Max Payne (2008)','Monty Python and the Holy Grail (1975)', 'Morning Departure (1950)',\
        'Mrtv mezi zivmi (1947)']}, 'The Knives (2020)')
    set()
    >>> find_film_keywords( {'20-th century' : ['The Gift (2005/I) (V)', 'The Glass House (2009)',\
        'The Hip Hop Hoax (2013)', 'The Hitchcock of HipHop (2008) (V)', 'The Label (2007) (V)'],\
        'classic' : ['Le divin enfant (2001) (TV)', 'Le feu follet (1963)',\
        'Le salaire de la peur (1953)', 'Lord Jim (1965)', 'Love and Death (1975)',\
        'Lulu on the Bridge (1998)', "M'Liss (1936)", 'Maps to the Stars (2014)',\
        'Max Payne (2008)','Monty Python and the Holy Grail (1975)', 'Morning Departure (1950)',\
        'Mrtv mezi zivmi (1947)']}, 'Le feu follet (1963)')
    {'classic'}
    >>> find_film_keywords( {'20-th century' : ['The Gift (2005/I) (V)', 'The Glass House (2009)',\
        'The Hip Hop Hoax (2013)', 'The Hitchcock of HipHop (2008) (V)', 'The Label (2007) (V)'],\
    'classic' : ['Le divin enfant (2001) (TV)', 'Le feu follet (1963)',\
        'Le salaire de la peur (1953)', 'Lord Jim (1965)', 'Love and Death (1975)',\
        'Lulu on the Bridge (1998)', "M'Liss (1936)", 'Maps to the Stars (2014)',\
        'Max Payne (2008)','Monty Python and the Holy Grail (1975)', 'Morning Departure (1950)',\
        'Mrtv mezi zivmi (1947)'],\
    'random keyword': [ '"Princess of Power" (1985)', '"Shoebox Zoo" (2004)', '"Shokuzai" (2012)',\
        '"Star Wars: Clone Wars" (2003)', '"Taboo" (2002)', '"The All-New Super Friends Hour"\
        (1977) {The Marsh Monster/Runaways/Will the World Collide?/Time Rescue (#1.3)}',\
        '"The Animals of Farthing Wood" (1993)', '"The Colour of Magic" (2008)']},\
        'The Hip Hop Hoax (2013)')
    {'20-th century'}
    """
    result = set()
    for key_word, list_with_films in film_keywords.items():
        if film_name in list_with_films:
            result.add(key_word)
    return result


def find_films_with_keywords(film_keywords: dict, num_of_films: int) :
    """
    Return list(tuple(str, int)) where str is a film name and\
    int is a number of keywords for that title
    >>> find_films_with_keywords( {'20-th century' : ['The Gift (2005/I) (V)',\
        'The Glass House (2009)', 'The Hip Hop Hoax (2013)', 'The Hitchcock of HipHop (2008) (V)',\
        'The Label (2007) (V)', "M'Liss (1936)"],\
    'classic' : ['Le divin enfant (2001) (TV)', 'Le feu follet (1963)',\
        'Le salaire de la peur (1953)', 'Lord Jim (1965)', 'Love and Death (1975)',\
        'Lulu on the Bridge (1998)', "M'Liss (1936)", 'Maps to the Stars (2014)',\
        'Max Payne (2008)','Monty Python and the Holy Grail (1975)', 'Morning Departure (1950)',\
        'Mrtv mezi zivmi (1947)', '"Star Wars: Clone Wars" (2003)'],\
    'random keyword': [ '"She-Ra: Princess of Power" (1985)', '"Shoebox Zoo" (2004)',\
        '"Shokuzai" (2012)', '"Star Wars: Clone Wars" (2003)', '"Taboo" (2002)',\
        '"The All-New Super Friends Hour" (1977) ', '"The Animals of Farthing Wood" (1993)',\
        '"The Colour of Magic" (2008)', 'The Hip Hop Hoax (2013)', "M'Liss (1936)"]}, 3 )
    [("M'Liss (1936)", 3), ('The Hip Hop Hoax (2013)', 2), ('"Star Wars: Clone Wars" (2003)', 2)]
    >>> find_films_with_keywords( {'20-th century' : ['The Gift (2005/I) (V)',\
        'The Glass House (2009)', 'The Hip Hop Hoax (2013)', 'The Hitchcock of HipHop (2008) (V)',\
        'The Label (2007) (V)', "M'Liss (1936)"],\
    'classic' : ['Le divin enfant (2001) (TV)', 'Le feu follet (1963)',\
        'Le salaire de la peur (1953)', 'Lord Jim (1965)', 'Love and Death (1975)',\
        'Lulu on the Bridge (1998)', "M'Liss (1936)", 'Maps to the Stars (2014)',\
        'Max Payne (2008)','Monty Python and the Holy Grail (1975)', 'Morning Departure (1950)',\
        'Mrtv mezi zivmi (1947)', '"Star Wars: Clone Wars" (2003)'],\
    'random keyword': [ '"She-Ra: Princess of Power" (1985)', '"Shoebox Zoo" (2004)',\
        '"Shokuzai" (2012)', '"Star Wars: Clone Wars" (2003)', '"Taboo" (2002)',\
        '"The All-New Super Friends Hour" (1977) ', '"The Animals of Farthing Wood" (1993)',\
        '"The Colour of Magic" (2008)', 'The Hip Hop Hoax (2013)', "M'Liss (1936)"]}, 1 )
    [("M'Liss (1936)", 3)]
    >>> find_films_with_keywords( {'20-th century' : ['The Gift (2005/I) (V)',\
        'The Glass House (2009)', 'The Hip Hop Hoax (2013)', 'The Hitchcock of HipHop (2008) (V)',\
        'The Label (2007) (V)', "M'Liss (1936)"],\
    'classic' : ['Le divin enfant (2001) (TV)', 'Le feu follet (1963)',\
        'Le salaire de la peur (1953)', 'Lord Jim (1965)', 'Love and Death (1975)',\
        'Lulu on the Bridge (1998)', "M'Liss (1936)", 'Maps to the Stars (2014)',\
        'Max Payne (2008)','Monty Python and the Holy Grail (1975)', 'Morning Departure (1950)',\
        'Mrtv mezi zivmi (1947)', '"Star Wars: Clone Wars" (2003)'],\
    'random keyword': [ '"She-Ra: Princess of Power" (1985)', '"Shoebox Zoo" (2004)',\
        '"Shokuzai" (2012)', '"Star Wars: Clone Wars" (2003)', '"Taboo" (2002)',\
        '"The All-New Super Friends Hour" (1977) ', '"The Animals of Farthing Wood" (1993)',\
        '"The Colour of Magic" (2008)', 'The Hip Hop Hoax (2013)', "M'Liss (1936)"]}, 0 )
    []
    """
    result = []
    title_dict = {}
    for list_names in film_keywords.values():
        for title in list_names:
            title_dict[title] = title_dict.get(title, 0) + 1
    new_dict = sorted(title_dict.items(), key = lambda pare : pare[1], reverse = True)
    counter = 1
    for name, number in new_dict:
        if counter > num_of_films:
            break
        result.append((name, number))
        counter += 1
    return result

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
