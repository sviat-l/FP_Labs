def caesar_encode(message, key):
    """
    (str, str) -> str
    Encode message by Ceasar code( shift letters in alphabet by n possitions
    where n is a key) with the given key. Return encoded message.
    >>> caesar_encode('cosmology' , 3)
    'frvprorjb'
    >>> caesar_encode('astronomy' , 11)
    'ldeczyzxj'
    >>> caesar_encode('result' , 42)
    'huikbj'
    """
    encode_message = ''
    for symbol in message:
        if  not symbol.isalpha():
            encode_message += symbol
        else:
            encode_message += chr ((ord(symbol) - 97 + key) % 26 + 97)

    return encode_message


def caesar_decode(message, key):
    """
    (str, str) -> str
    Decode message by Ceasar code( shift letters in alphabet by n possitions
    where n is a key) with the given key. Return decoded message.
    >>> caesar_decode("hzayvsvnf", 7)
    'astrology'
    >>> caesar_decode("mjovy" , 1)
    'linux'
    >>> caesar_decode("ejokijew" , 100)
    'insomnia'
    """
    decode_message = ''
    for symbol in message:
        if  not symbol.isalpha():
            decode_message += symbol
        else:
            decode_message += chr ((ord(symbol) - 97 - key) % 26 + 97)

    return decode_message


print(caesar_encode('cosmology' , 3))
print(caesar_decode("frps xwhu", 29))



