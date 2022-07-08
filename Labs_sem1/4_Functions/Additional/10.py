def encrypt_message(s):
    """
    str -> str
    Replace all letters in string with next letters in aplhabet. If argument is not a string
    function should return None.

    >>> encrypt_message("Revenge is a dish that tastes best when served cold.")
    Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.
    >>> encrypt_message("Never hate your enemies. It affects your judgment.")
    Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.
    >>> encrypt_message(2015)

    """
    if type(s) != str:
        return None
    output=''
    for symbol in s:
        if 90>(ord(symbol))>64 or 122>ord(symbol)>96:
            output+=chr(ord(symbol)+1)
        elif ord(symbol) in  [90, 122]:
            output+=chr(ord(symbol)-25) 
        else:
            output+=symbol
    return output

print(encrypt_message(" a A z Z"))
#done
