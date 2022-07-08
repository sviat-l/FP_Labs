def exclude_letters(s1, s2):
    """
    (str, str) -> str
    Delete all letter from string s2 in string s1. If arguments aren't strings function should
    return None.

    >>> exclude_letters("aaabb", "b")
    aaa
    >>> exclude_letters("abcc", "cczzyy")
    ab
    >>> exclude_letters(2015, "sasd")

    """
    if type(s1)!=str or type(s2)!=str:
        return None
    text1=list(s1)

    for letter in s2:
        text1=[let for let in text1 if let!=letter]

    return ('').join(text1)

print(exclude_letters("aaabb", "b"))

#done
    