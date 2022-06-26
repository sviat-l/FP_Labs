"""
Lab 3.3 Classroom
"""

class Classroom:
    """ Class to safe information related to the Classroom
    >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_016.number
    '016'
    >>> classroom_016.capacity
    80
    >>> classroom_016.equipment
    ['PC', 'projector', 'mic']

    >>> print(classroom_016)
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.

    >>> classroom_007 = Classroom('007', 12, ['TV'])
    >>> classroom_016.is_larger(classroom_007)
    True
    >>> classroom_016.equipment_differences(classroom_007)
    ['PC', 'mic', 'projector']

    >>> classroom_016
    Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> [classroom_016]
    [Classroom('016', 80, ['PC', 'projector', 'mic'])]
    """

    def __init__(self, number:str, capacity:int, equipment:list) -> None:
        """ Iniitialize Building data """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self) -> None:
        """ String representaion of the self
        return string with self paramaters data """
        return f'{self.__class__.__name__} {self.number} has a capacity of {self.capacity} persons and has the following equipment: {", ".join(self.equipment)}.'

    def is_larger(self, other) -> bool:
        """ Check if self is larger (has bigger capacity) """
        return self.capacity > other.capacity

    def equipment_differences(self, other) -> list[str]:
        """ Return equipment from self that is not other Classroom object in the ASCII order """
        return sorted(list(set(self.equipment) - set(other.equipment)))

    def __repr__(self) -> str:
        """ represent method, show classroom parameters"""
        return f"{self.__class__.__name__}('{self.number}', {self.capacity}, {self.equipment})"

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
