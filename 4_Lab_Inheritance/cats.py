"""
Lab 4.2  Cats
"""


class Animal:
    """ Class to work with the animal data

    >>> animal1= Animal("chordata", "mammalia")
    >>> animal1.phylum
    'chordata'
    >>> animal1.clas
    'mammalia'
    >>> str(animal1)
    '<animal class is mammalia>'
    >>> animal2 = Animal("chordata", "birds")
    >>> animal1 == animal2
    False
    """

    def __init__(self, phylum:str, clas:str) -> None:
        """ Init animal variables """
        self.phylum = phylum
        self.clas = clas

    def __str__(self) -> str:
        """ String representaion of the self """
        return f'<animal class is {self.clas}>'

    def __eq__(self, other: object) -> bool:
        return self.phylum == other.phylum and self.clas == other.clas

class Cat(Animal):
    """ Class related to the cats

    >>> cat1 = Cat("chordata", "mammalia", "felis")
    >>> cat1.sound()
    'Meow'
    >>> cat1.genus
    'felis'
    >>> isinstance(cat1, Animal)
    True
    >>> str(cat1)
    '<This felis animal class is mammalia>'
    """

    def __init__(self, phylum: str, clas: str, genus:str) -> None:
        """ Init cat's data"""
        super().__init__(phylum, clas)
        self.genus = genus

    def __str__(self) -> str:
        """ String representation of self"""
        return f'<This {self.genus} animal class is {self.clas}>'

    def sound(self) -> None:
        """ Return string with cats sound"""
        return 'Meow'


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
