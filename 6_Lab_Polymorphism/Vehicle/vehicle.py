"""
Lab 6.2 Vehicle
"""

class Vehicle:
    """ Basic Vehicle class """

    def __init__(self, brand:str, model:str, tipe:str, gas_tank_size = 0, fuel_consumption=6) -> None:
        """
        Init class variables with default fuel_level as 0 and fuel_consumption default as 6
        """
        self.brand = brand
        self.model = model
        self.tipe = tipe
        self.gas_tank_size = gas_tank_size
        self.fuel_consumption = fuel_consumption
        self.fuel_level = 0

    def fuel_up(self, add_part:int):
        """ Add stated number of fuel to the tank """
        self.fuel_level = min(self.gas_tank_size, self.fuel_level + add_part)
        return "Gas tank is filled."

    def get_fuel_level(self):
        """ Return current fuel level """
        return self.fuel_level

    def drive(self, distance:int):
        """ If there is enough fuel drive stated distance, change fuel_level
        Otherwise return string information """
        used_fuel = self.fuel_consumption * distance/100
        if used_fuel > self.fuel_level:
            return "Not enough fuel level in a gas tank."
        self.fuel_level -= used_fuel
        return f'The {self.brand} {self.model} is now driving.'

    def __str__(self) -> str:
        """ String representation of self with info about class object """
        return f"Vehicle {self.brand} {self.model} is a {self.tipe}." + \
        (f" It has a gas tank size of {self.gas_tank_size}." if self.gas_tank_size else '')


class Battery:
    """ Class with information related to the car Battery """

    def __init__(self, charge_size=85, charge_level=0) -> None:
        """ Init battery values with charge_size default as 85, and charge_level default as 0 """
        self.charge_size = charge_size
        self.charge_level = charge_level

    def __str__(self) -> str:
        """ String representaion of self """
        return f'Battery has size of {self.charge_size}, it is charged up to {self.charge_level}%'

    def get_charge_level(self):
        """ Return charge level of the battery """
        return self.charge_level

    def set_charge_level(self, new_level:int):
        """ Change battery level to new_level """
        self.charge_level = new_level


class ElectricVehicle(Vehicle):
    """ Electric vehicle is subclass of Vehicle """

    def __init__(self, brand: str, model: str, tipe: str) -> None:
        Vehicle.__init__(self, brand, model, tipe)
        self.battery = Battery()

    def charge(self):
        """ Change battery level """
        self.battery.set_charge_level(100)
        return "The vehicle is fully charged."

    def get_charge_level(self):
        """ Return battey charge level """
        return self.battery.get_charge_level()

    def drive(self):
        """ Drive untill battery is not discharged """
        self.battery.set_charge_level(0)
        return f'The {self.brand} {self.model} is now driving.'

    def get_battery_info(self) -> str:
        """ Return string with information about Battery state """
        return str(self.battery)
