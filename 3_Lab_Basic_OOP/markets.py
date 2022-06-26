"""
Lab 3.2 Markets
"""

class Markets:
    """"
    Market class implementation. Contains data about market

    >>> market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
    >>> market_family_food.name
    'Family Food'
    >>> market_family_food.area
    80
    >>> market_family_food.categories
    ['Bread and Bakery', 'Dairy', 'Beverages']

    >>> print(market_family_food)
    Supermarket Family Food has an area of 80 m2 and has the following categories: Bread and Bakery, Dairy, Beverages.
    """

    def __init__(self, name, area, categories) -> None:
        """Init values related to the market"""
        self.name = name
        self.area = area
        self.categories = categories


    def __str__(self) -> str:
        """ String representaion of self. Print all self parameters"""
        return f'Supermarket {self.name} has an area of {self.area} m2 and has the following categories: {", ".join(self.categories)}.'

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
