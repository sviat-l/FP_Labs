"""
Exam task 1.2 Letters
"""


class First:
    """
    First class.
    Get vowels and consonants
    """

    def __init__(self, line: str) -> None:
        """
        Init function
        """
        self.vowels, self.consonants = [], []
        for letter in line:
            if letter in 'eyuioa':
                self.vowels.append(letter)
            else:
                self.consonants.append(letter)

    def __str__(self) -> str:
        """
        String representation of self
        """
        return f'{self.__class__.__name__}(consonants={self.consonants}, vowels={self.vowels})'

    def __eq__(self, other: object) -> bool:
        """ Check if self equels other """
        return isinstance(other, First) and self.consonants == other.consonants

    def clear_vowels(self) -> None:
        """
        Clear vowels of the self object
        """
        self.vowels = []

    def cleared_vowels(self) -> object:
        """
        Return class object without vowels
        """
        return First(''.join(self.consonants))


class Second(First):
    """
    Second class is the subclass of the First
    """

    def __init__(self, line: str, shift_number) -> None:
        """ Init method """
        super().__init__(line)
        self.shift_number = shift_number

    def __str__(self) -> str:
        """
        String rerpesentaion of self
        """
        return f'{self.__class__.__bases__[0].__name__}(consonants={self.consonants}, vowels={self.vowels})'

    def encoder(self):
        """
        Return Second class object with
        letters shifted on stated number
        """
        shifted = [chr((ord(s) - ord('a') + self.shift_number) % 26
                       + ord('a')) for s in self.consonants]
        for s in self.vowels:
            shifted.append(chr((ord(s) - ord('a') +
                                self.shift_number) % 26 + ord('a')))
        return Second(''.join(shifted), self.shift_number)
