"""
Lab 3.7 Logistic System with basic functionality
"""

# global variable last id to track id numbers
LAST_ID = 1000000

class Location:
    """ Class to save data about Locations """

    def __init__(self, city:str, postoffice: int) -> None:
        """ Init location's city and postoffice number """
        self.city = city
        self.postoffice = postoffice

    def __str__(self) -> str:
        """ String representation of self """
        return f' Posoffice in {self.city} #{self.postoffice}'

class Item:
    """ Class with methods related to an item """
    def __init__(self, name:str, price:int) -> None:
        """ Init item's values """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """ String representation of self """
        return f'Item {self.name} with price {self.price}'


class Vehicle:
    """ Class to save data about the vehicle """

    def __init__(self, vehicleNo:int, isAvailable=True) -> None:
        """ Init vehicle information """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable

    def __str__(self) -> str:
        """ String representation of self """
        return f'Vehicle number{self.vehicleNo} is {"" if self.isAvailable else "not"} availiable'


class Order:
    """ Main class related to one order information and its tracking"""

    def __init__(self, user_name:str, city:str, postoffice:int, items:list[Item]) -> None:
        """ Init order information """
        global LAST_ID
        self.orderId = LAST_ID
        LAST_ID += 1
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None

    def __str__(self) -> str:
        """ String representation of self """
        return f'Your order #{self.orderId} is sent to {self.location}. Total price: {self.calculateAmount()}'

    def calculateAmount(self) -> float:
        """ Calculate and return total price of the order"""
        return round(sum(item.price for item in self.items),2)


    def assignVehicle(self, vehicle:Vehicle) -> None:
        """ Assign Vehicle for the order """
        self.vehicle = vehicle


class LogisticSystem:
    """ Main class to run Logistic system with users and their orders"""

    def __init__(self, vehicles:list[Vehicle]) -> None:
        """ Init class values, and empty dict with oreders id:order """
        self.vehicles = vehicles
        self.orders = {}

    def placeOrder(self, order: Order) -> None:
        """ Add order in a row if there is an availiable vehicle
            Otherwise, inform the user that vehicle was not found
        """
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                order.vehicle = vehicle
                vehicle.isAvailable = False
                self.orders[order.orderId] = order
                return print(f'Order was send on vehicle: {vehicle.vehicleNo}')
        return print('There are no available vehicles. Please wait...')

    def trackOrder(self, order_id: int) -> str:
        """ Return information about order if it exists.
            Otherwise, inform the user that order was not found
        """
        print(str(self.orders[order_id]) if order_id in self.orders else 'No such order.' )


def test_cases():
    """
    Function to run tests and show logistic system usage
    """

    location = Location('Lviv', 79001)
    print(location)
    vehicle = Vehicle(1)
    print(vehicle)
    vehicle.isAvailable = False
    print(vehicle)
    item = Item('Book', 99.90)
    print(item)
    print()

    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item('book',110), Item('chupachups',44)]
    my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
    logSystem.placeOrder(my_order)
    logSystem.trackOrder(1000000)

    my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    logSystem.placeOrder(my_order2)
    logSystem.trackOrder(1000001)

    my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
    my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    logSystem.placeOrder(my_order3)
    logSystem.trackOrder(1000002)


if __name__ == '__main__':
    test_cases()
