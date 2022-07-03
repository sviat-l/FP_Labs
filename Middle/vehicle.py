"""
Middle2 Vehicle
"""

class Passenger:
    """
    Class related to the vehicle passenger
    """
    def __init__(self, name:str) -> None:
        """
        Init passanger with default None vehicle
        """
        self.name = name
        self._Passenger__place = None

    @property
    def place(self):
        """ param place is _Passenger__place """
        return self._Passenger__place

    @place.setter
    def place(self, value):
        """ Setter for place"""
        self._Passenger__place = value


    def __str__(self) -> str:
        """ String representaton of self """
        return f'{self.name} is passenger of {"..." if self.place is None else self.place.name }'


class Driver(Passenger):
    """ Passenger who can drive """


class Vehicle:
    """
    Main vehicle class
    """

    def __init__(self, name:str, capasity:int) -> None:
        """
        Init class parameters with empty passenger list at the begining
        """
        self.name = name
        self.capasity = capasity
        self.passengers = []

    def __str__(self) -> str:
        """
        String representation of self
        """
        return f'{self.name} holds {self.capasity}: '\
               f'{[passanger.name for passanger in self.passengers]}, '\
               f'free {self.capasity - len(self.passengers)}'

    def is_empty(self) -> bool:
        """ Chech if vehicle is empty """
        return not self.passengers

    def add_passenger(self, passenger:Passenger) -> bool:
        """
        Add passanger. Return True if it is possible, otherwise False
        """
        if len(self.passengers) != self.capasity and passenger.place != self:
            self.passengers.append(passenger)
            passenger.place = self
            return True
        return False

    def remove_passenger(self) -> Passenger|tuple:
        """
        Remove the recent passanger from the vehicle,
        if it is possible. Otherwise return False.
        """
        if self.is_empty():
            return False
        removed = self.passengers.pop()
        removed.place = None
        return (removed, f'{self.name} is empty!') if self.is_empty() else removed


    def __hash__(self) -> int:
        """
        Hash operator. Hash vehicle name, capacity and passangers
        """
        return hash((self.name, self.capasity, tuple(self.passengers)))


class Bus(Vehicle):
    """
    Bus class as subclass of Vehicle
    """
    def __init__(self, name: str, capasity: int, path:str) -> None:
        """ Init Bus values """
        super().__init__(name, capasity)
        self.path = path

    def __eq__(self, other: object) -> bool:
        """ Check if self equels other """
        return isinstance(other, Bus) and ((self.name, self.capasity, self.path) ==
                                           (other.name, other.capasity, other.path))

    def __hash__(self) -> int:
        """
        Hash operator. Get hash of the bus name, capacity, passengers and path
        """
        return hash((self.name, self.capasity, tuple(self.passengers), self.path))


class Buggy(Vehicle):
    """
    Buggy class is a Vehicle subclass.
    Change number of buggies created.
    """
    BUGGIECOUNT = 0


    def __init__(self, name: str) -> None:
        """
        Init vehicle with capasity=1, and pushing is False
        """
        super().__init__(name, 1)
        self.pushing = False
        self.number = Buggy.BUGGIECOUNT
        Buggy.BUGGIECOUNT += 1


    def start_pushing(self) -> None:
        """ Start pushing a buggy """
        self.pushing = True

    def stop_pushing(self) -> None:
        """ Stop pushing a buggy """
        self.pushing = False

    @staticmethod
    def buggy_count() -> None:
        """ Return # number buggies created """
        return Buggy.BUGGIECOUNT

    def remove_passenger(self) -> bool|Passenger:
        """
        Remove passanger from the vehicle.
        Can not remove if buggy is pushing
        """
        if self.pushing or self.is_empty():
            return False
        removed = self.passengers.pop()
        removed.place = None
        return removed

    def __eq__(self, other: object) -> bool:
        """ Check if self equels other """
        return isinstance(other, Buggy) and self.name == other.name

    def __hash__(self) -> int:
        """ Hash operator. Hash buggie name """
        return hash(self.name)
