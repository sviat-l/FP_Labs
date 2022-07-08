def decrypt_message(s):
    """
    str -> str
    'Replace all letters in string with previous letters in aplhabet. If argument isn't a string
    function should return None.'

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    'Revenge is a dish that tastes best when served cold.'
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    'Never hate your enemies. It affects your judgment.'
    >>> decrypt_message(2015)

    >>> decrypt_message("Letter a is in this text")
    'Kdssdq z hr hm sghr sdws'
    """
    if type(s) != str :
        return None

    output=''

    for symbol in s:
        if 91>(ord(symbol))>65 or 123>ord(symbol)>97:  
            output+=chr(ord(symbol)-1)
        elif ord(symbol) in  [65, 97]:
            output+=chr(ord(symbol)+25) 
        else:
            output+=symbol

    return output
    

print(decrypt_message("Letter a is in this text"))

#done

#  a-z problem
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())