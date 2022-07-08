def find_intersection(s1, s2):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    b
    >>> find_intersection("aZAbc", "zzYYxp")
    z
    >>> find_intersection("sfdfsdf", 2015)

    """
    if (type(s1) or type(s1)) != str:
        return None
        
    output=''

    for position in range(97,123):
        if (chr(position) in s1) or (chr(position-32) in s1):
             if (chr(position) in s2) or (chr(position-32) in s2):
                 output+=chr(position)

    return output

print(find_intersection("aZAbc", "zzYYxp"))

#done        