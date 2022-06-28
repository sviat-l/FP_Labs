"""
Lab 6.4 Birds
"""


class Egg:
    """ Empty egg class """

class Bird:
    """
    Class with data and methods related to the bird
    """

    def __init__(self, name:str) -> None:
        """ Init bird name and set eggs as list() """
        self.name = name
        self.eggs = []

    def lay_egg(self):
        """ Add new egg to eggs """
        self.eggs.append(Egg())

    def fly(self):
        """ return string information about fly ability """
        return 'I can fly!'

    def count_eggs(self):
        """ Return total number of eggs """
        return len(self.eggs)

    def get_eggs(self):
        """ Return list with eggs """
        return [egg for egg in self.eggs]

    def __repr__(self):
        """
        Represent method
        """
        return f'{self.name} has {self.count_eggs()} egg{"s" if self.count_eggs()!=1 else ""}'


class Penguin(Bird):
    """
    Class Penguin subclass of Bird class
    """
    def fly(self):
        """ return string information about fly ability """
        return 'No flying for me.'

    def swim(self):
        """ return string information about swimm ability """
        return 'I can swim!'


class MessengerBird(Bird):
    """
    Class MessengerBird subclass of Bird class
    """
    def __init__(self, name:str, message='') -> None:
        """ Init method """
        super().__init__(name)
        self.message = message

    def deliver_message(self):
        """ return messenger bird message """
        return self.message
