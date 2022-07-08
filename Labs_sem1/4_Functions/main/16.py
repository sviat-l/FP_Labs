def find_union(s1, s2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'AYZabcpxz'
    >>> find_union("sfdfsdf", 2015)

    """
    if type(s1)!=str or type(s2)!=str:
        return None

    output=''
    for ord_letter in range(65,91):
        letter=chr(ord_letter)
        if letter in s1  or  letter in s2 :
            output+= letter

    for ord_letter in range(97,123):
        letter=chr(ord_letter)
        if letter in s1  or  letter in s2 :
            output+= letter
    return output

print(find_union("aZAbc", "zzYYxp"))
#done

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())