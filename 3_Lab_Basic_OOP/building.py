"""
Lab 3.4 Academic Building
"""
import classroom

class AcademicBuilding:
    """
    Class with method releated to the Builinding data

    >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
    >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)

    >>> building.address
    'Kozelnytska st. 2a'
    >>> for room in building.classrooms:
    ...     print(room)
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
    Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
    Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.

    >>> building.total_equipment()
    [('PC', 2), ('TV', 1), ('mic', 1), ('projector', 2)]

    >>> print(building)
    Kozelnytska st. 2a
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
    Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
    Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
    """
    def __init__(self, address, classrooms:list[classroom.Classroom]) -> None:
        """ Init method """
        self.address = address
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


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
