"""
Middle2 Vehicle Tests
"""

import unittest
from vehicle import Vehicle, Bus, Passenger, Buggy, Driver


class VehicleTests(unittest.TestCase):
    """
    Class with pytests for vehecle module
    """

    def test1Creating(self):
        """
        Tets creation of Vehcile and Passanger objects
        and their __str__ methods
        """
        # a vehicle has a name and a capacity
        VehicleTests.v1 = Vehicle("Zorith", 2)
        assert(str(VehicleTests.v1) == "Zorith holds 2: [], free 2")
        assert VehicleTests.v1.is_empty() == True
        VehicleTests.p1 = Passenger('Arman')
        VehicleTests.p2 = Passenger('Armana')
        assert str(VehicleTests.p1) == "Arman is passenger of ..."

    def test2AddRemove(self):
        """
        Test adding and removing passangers from the vehicle
        and Passanger parameters
            add_passenger()
            remove_passenger()
            .place
            ._Passenger__place
        """
        # passengers can be added
        assert(VehicleTests.v1.add_passenger(VehicleTests.p1) == True)
        assert(VehicleTests.p1.place == VehicleTests.v1)
        assert(VehicleTests.p1._Passenger__place == VehicleTests.v1)
        assert str(VehicleTests.p1) == "Arman is passenger of Zorith"
        assert(VehicleTests.v1.add_passenger(VehicleTests.p1) == False)
        assert(VehicleTests.v1.add_passenger(VehicleTests.p2) == True)
        # can't add passengers past the max capacity
        VehicleTests.p3 = Passenger("Arcana")
        assert(VehicleTests.v1.add_passenger(VehicleTests.p3) == False)
        assert(str(VehicleTests.v1) ==
               "Zorith holds 2: ['Arman', 'Armana'], free 0")
        # can remove the most recent passenger
        assert(VehicleTests.v1.remove_passenger() == VehicleTests.p2)
        assert(str(VehicleTests.v1) == "Zorith holds 2: ['Arman'], free 1")
        assert(VehicleTests.v1.add_passenger(VehicleTests.p3) == True)

    def test3Bus(self):
        """
        Test Bus class as Vehicle subclass
            add_passanger()
            remove_passanger()
            __eq__
        """
        # a bus has a name, a capacity and a path
        path = "Lviv - Stari Kuty"
        VehicleTests.v2 = Bus("Bus", 20, path)
        # can't remove a passenger from an empty bus or vehicle
        assert(VehicleTests.v2.remove_passenger() == False)
        assert(VehicleTests.v2.add_passenger(VehicleTests.p2) == True)
        assert(str(VehicleTests.v2) == "Bus holds 20: ['Armana'], free 19")
        assert VehicleTests.v2.remove_passenger() == (VehicleTests.p2, "Bus is empty!")

        # two buses can be compared
        assert(VehicleTests.v2 == Bus("Bus", 20, path))
        assert(VehicleTests.v2 != Bus("Bus", 20, "Lviv - Tuziliv"))
        assert(VehicleTests.v2 != VehicleTests.v1)
        assert(VehicleTests.v2 != "Bus")  # should not crash!

    def test4Buggy(self):
        """
        Test buggy class:
            add_passanger()
            remove_passanger()
            pushing (start, stop)
            buggy_count()
        """
        # a buggy is a vehicle with a name and an assumed capacity of 1
        VehicleTests.b1 = Buggy("ADC Buggy")
        VehicleTests.p4 = Driver("Driver")
        assert(VehicleTests.b1.add_passenger(VehicleTests.p4) == True)
        assert(VehicleTests.p4.place == VehicleTests.b1)
        assert(str(VehicleTests.b1) == "ADC Buggy holds 1: ['Driver'], free 0")
        # a buggy knows whether it's currently being pushed
        VehicleTests.b1.start_pushing()
        # while it's being pushed, you can't remove passengers
        # don't worry about adding passengers while pushing
        assert(VehicleTests.b1.remove_passenger() == False)
        VehicleTests.b1.stop_pushing()
        # when the buggy is stopped, normal rules apply
        assert(VehicleTests.b1.remove_passenger() == VehicleTests.p4)
        assert(VehicleTests.b1.remove_passenger() == False)
        VehicleTests.b2 = Buggy("SD Buggy")
        VehicleTests.b3 = Buggy("DC Buggy")
        assert VehicleTests.b2 == Buggy("SD Buggy")
        assert VehicleTests.b2 != VehicleTests.b3
        assert Buggy.buggy_count() == 4

    def tets5Garage(self):
        """
        Tets hash methods for Vehicle classes
            __hash__
        """
        # a garage is a set of vehicles
        VehicleTests.b1 = Buggy("ADC Buggy")
        VehicleTests.v1 = Vehicle("Zorith", 2)
        garage = set()
        assert VehicleTests.v1 not in garage
        garage.add(VehicleTests.v1)
        assert VehicleTests.v1 in garage
        assert VehicleTests.b1 not in garage
        garage.add(VehicleTests.b1)
        assert VehicleTests.b1 in garage
        garage.remove(VehicleTests.b1)
        assert VehicleTests.b1 not in garage


if __name__ == '__main__':
    unittest.main()
