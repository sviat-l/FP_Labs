"""
Exam task 1.1 Numbers
"""

class First:
    """
    Frist class takes variable of arguments
    """

    def __init__(self, *args:int) -> None:
        """
        Init even and odds variables taken
        from the arguments. Evens are sorted
        """
        self.evens, self.odds = [], []
        for number in args:
            if number&1:
                self.odds.append(number)
            else:
                self.evens.append(number)
        self.evens.sort()


    def __str__(self) -> str:
        """ String representaion of self """
        return f'{self.__class__.__name__}(evens={self.evens}, odds={self.odds})'

    def __eq__(self, other: object) -> bool:
        """ Check if self equels other """
        return isinstance(other, First) and self.evens == other.evens

    def del_odds(self) -> None:
        """
        Delete odds from self object
        """
        self.odds = []

    def deleted_odds(self):
        """
        Create and return new object without odd numbers
        """
        return First(*self.evens)


class Second(First):
    """
    Second class is First subclass.
    Takes arguments as its range numbers
    """

    def __init__(self, lower:int, higher:int) -> None:
        """ Init function """
        super().__init__(*range(lower, higher+1))
        self.lower = lower
        self.higher = higher

    def __str__(self) -> str:
        """
        String representation of self
        """
        return f'{self.__class__.__bases__[0].__name__}(evens={self.evens}, odds={self.odds})'

    def transform(self, value:int):
        """
        Create and return Second class object
        with trasformed range numbers (+value)
        """
        return Second(self.lower+value, self.higher+value)
