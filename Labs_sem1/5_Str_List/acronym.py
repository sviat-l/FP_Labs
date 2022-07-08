def create_acronym(message):
    """
    Create  acronyms to the phrases of the text which are divided by new-line symbol
    Return acronyms and its meaning.
    >>> print(create_acronym("random access memory\\nAs soon As possible"))
    RAM - random access memory
    ASAP - As soon As possible
    >>> print(create_acronym("North Atlantic Treaty Organization\\nEuropean union\\nUnited Kingdom"))
    NATO - North Atlantic Treaty Organization
    EU - European union
    UK - United Kingdom
    >>> print(create_acronym("International Mathematical Olympiad"))
    IMO - International Mathematical Olympiad
    """
    phrases = [message[0]]

    if message[0] != ' ':
        acronyms = [message[0].upper()]
    else:
        acronyms = ['']

    symbol_number = len(message)
    for i in range(symbol_number - 1):
        if (message[i] == ' '  and message[i+1] != ' '):
            acronyms[-1] += message[i+1].upper()

        if message[i] == '\n':
            acronyms.append(message[i+1].upper())
            phrases.append('')

        phrases[-1] += message[i+1]

    output = ''
    phrase_number = len(phrases)
    for j in range(phrase_number):
        output += f'{acronyms[j]} - {phrases[j]}'

    return output


print(create_acronym("International Mathematical Olympiad"))

if __name__ == '__main__':
    import doctest
    print(doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE))
