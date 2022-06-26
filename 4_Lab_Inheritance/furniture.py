"""
Lab 4.3 Furniture
"""

class Furniture:
    """ Class to store furniture data

    >>> furniture1 = Furniture('empire', 'bedroom')
    >>> furniture1.style
    'empire'
    >>> furniture1.assign
    'bedroom'
    >>> str(furniture1)
    '<furniture style is empire>'
    >>> furniture2 = Furniture('modern', 'bathroom')
    >>> furniture1 == furniture2
    False
    """

    def __init__(self, style:str, assign:str) -> None:
        """ Initialize furnitures values """
        self.style = style
        self.assign = assign

    def __eq__(self, other: object) -> bool:
        """ Check if self equels other """
        if not isinstance(other, Furniture):
            return False
        return (self.style, self.assign) == (other.style, other.assign)

    def __str__(self) -> str:
        """ String representation of self """
        return f'<furniture style is {self.style}>'


class Chair(Furniture):
    """ Chair class inherite Furniture class

    >>> chair1 = Chair('empire', 'bedroom', 'armchair')
    >>> isinstance(chair1, Furniture)
    True
    >>> chair1.tipe
    'armchair'
    >>> str(chair1)
    '<This armchair furniture style is empire>'
    >>> chair1.get_assign()
    'bedroom'
    """

    def __init__(self, style: str, assign: str, tipe:str) -> None:
        """ Init values. Get style and assign as init values of inherited class"""
        super().__init__(style, assign)
        self.tipe = tipe

    def get_assign(self) -> str:
        """ Return self's assigh"""
        return self.assign

    def __str__(self) -> str:
        """ String representation of self """
        return f'<This {self.tipe} furniture style is {self.style}>'


if __name__ =='__main__':
    import doctest
    print(doctest.testmod())
