"""
Lab 7.2 Flowers
"""

class Flower:
    """ Main class related to flower """

    def __init__(self, color:str, petals:int, price:int) -> None:
        """ Init flower's values"""
        self.color = color
        self.petals = petals
        self.price = price
        self.correct_values()

    def correct_values(self) -> None:
        """
        Check if values are in accordance to the rules
        Raise: TypeError or ValueError
        """
        if not isinstance(self.color, str):
            raise TypeError('Invalid type value of color parameter')
        if not isinstance(self.petals, int):
            raise TypeError('Invalid type value of petals parameter')
        if not isinstance(self.price, int):
            raise TypeError('Invalid type value for color parameter')
        if self.petals < 0:
            raise ValueError('Invalid patail value')
        if self.price < 0:
            raise ValueError('Invalid price value')


class Tulip(Flower):
    """ Tulip class. Subclass of the Flower """

    def __init__(self, petals, price):
        """ Init class values with default superclass color = 'pink' """
        super().__init__('pink', petals, price)


class Rose(Flower):
    """ Rose class. Subclass of the Flower """

    def __init__(self, petals, price):
        """ Init class values with default superclass color = 'red' """
        super().__init__('red', petals, price)


class Chamomile(Flower):
    """ Chamomile class. Subclass of the Flower """

    def __init__(self, petals, price):
        """ Init class values with default superclass color = 'white' """
        super().__init__('white', petals, price)


class FlowerSet:
    """ FlowerSet class.
        Provides adding flower to the set
    """

    def __init__(self) -> None:
        """ Init values with default flower_set as set() """
        self.flower_set = set()
        self.set_type = None

    def add_flower(self, flower:Flower):
        """
        Add the flower to the set
        Predictions: all flowers in the set have the same type
        Raise: TypeError if adding flower of wrong type
        """
        if self.set_type is None:
            self.set_type = type(flower)
        elif self.set_type != type(flower):
            raise TypeError('Invalid flower type for the set')
        self.flower_set.add(flower)

class Bucket:
    """
    Class to store data about the bucket and calculate its price
    """

    def __init__(self):
        """ Init starting bucket as list() """
        self.bucket = []

    def add_set(self, flower_set:FlowerSet):
        """ Add set with one type flowers to the bucket """
        self.bucket.append(flower_set)

    def total_price(self):
        """ Calculate and return total price of the bucket """
        return sum(sum(flower.price for flower in flowerSet.flower_set)\
                                    for flowerSet in self.bucket)
