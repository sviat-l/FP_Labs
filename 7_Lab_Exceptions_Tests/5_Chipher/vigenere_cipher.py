"""
Lab 7.5 Vigenere Cipher
"""

def combine_character(plain:str, keyword:str) -> str:
    """
    Return encoded letter from stated plain and keyword letters
    """
    return chr(ord('A') + (ord(plain.upper()) + ord(keyword.upper()) - 2*ord('A'))%26)


def separate_character(cypher:str, keyword:str) -> str:
    """
    Return decoded letter from stated cypher and keyword letters
    """
    return chr(ord('A') + (ord(cypher.upper()) - ord(keyword.upper()))%26)


class VigenereCipher:
    """
    Class to encode and decode message with vinegere cipher
    """
    def __init__(self, keyword:str) -> None:
        """ Init Vingere cipher keyword """
        self.keyword = keyword

    def extend_keyword(self, number:int) -> str:
        """
        Return extended plaintext to stated length
        """
        return (self.keyword * (number//len(self.keyword)+1))[:number]

    def encode(self, plaintext:str) -> str:
        """
        Encode text with self keyword
        """
        plaintext = plaintext.replace(' ', '')
        keyword = self.extend_keyword(len(plaintext))
        return ''.join([combine_character(p, k) for p,k in zip(plaintext, keyword)])

    def decode(self, cypher_text:str) -> str:
        """
        Decode cyper text with self keyword
        """
        keyword = self.extend_keyword(len(cypher_text))
        return ''.join([separate_character(c, k) for c,k in zip(cypher_text, keyword)])
