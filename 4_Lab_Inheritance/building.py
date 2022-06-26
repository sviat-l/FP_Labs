"""
Lab 4.1 Buildings
"""

class Building:
    """ Class to store building data """

    def __init__(self, address:str) -> None:
        """ Init building address"""
        self.address = address

class House(Building):
    """ Class to store house data """

    def __init__(self, address:str, appartments:list) -> None:
        super().__init__(address)
        self.appartments = appartments



class AcademicBuilding(Building):
    """
    Class with method releated to the Builinding data
    """
    def __init__(self, address:str, classrooms:list) -> None:
        """ Init method """
        super().__init__(address)
        self.classrooms = classrooms

    def total_equipment(self) -> list[tuple[str, int]]:
        """ Return list with total equipment in the Building.
        Contains tuples (names, numbers), sorted in the alphabet orded """
        equipment_dict = {}
        for room in self.classrooms:
            for item in room.equipment:
                equipment_dict[item] = equipment_dict.get(item, 0) + 1

        return sorted([(name, number) for name, number in equipment_dict.items()])

    def __str__(self) -> str:
        """ String representaion of the building.
            Print address and classrooms info
        """
        return '\n'.join([self.address] + [str(room) for room in self.classrooms])

class Classroom:
    """ Class to safe information related to the Classroom """

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
