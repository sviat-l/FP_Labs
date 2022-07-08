def number_of_occurence(lst, s):
    """
    (list, str) -> int
    Find and return number of occurence of string s in all elements of the
    list lst. If lst isn't list of strings or s isn't string function should
    return None.

    >>> number_of_occurence(["man", "girl", "women", "boy"], "m")
    2
    >>> number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba")
    2
    >>> number_of_occurence([1, 2, 2015, 1, 3], "1")

    """
    if type(s) != str:
        return None
    occurence=0
    for word in lst:
        if type(word)!=str:
            return None
        occurence+=word.count(s)

    return occurence

#with overlapping:
"""
        for position_in_word in range(len(word) - len(s)+1):
                if word[position_in_word:position_in_word+len(s)]==s:
                    occurence+=1
"""
    

print(number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba"))
#done    