"""
Lab 4.4 Point, Point3D
"""

from math import sqrt

class Point:
    """ Class to save and proccess data about Point in two dimensional space"""

    def __init__(self, x_var:float, y_var:float) -> None:
        """ Initialize (x, y) point coordinates"""
        self.x = x_var
        self.y = y_var

    def __str__(self) -> str:
        """ String representation of self """
        return f'Point in two-dimensional space with coordinates ({self.x}, {self.y})'

    def __repr__(self) -> str:
        """ Represent method """
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other:object) -> bool:
        """ Check if self equels other """
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def vector_length(self) -> float:
        """ Calculate and return vector length """
        return round(sqrt((self.x ** 2 + self.y ** 2)), 2)



class Point3D(Point):
    """ Class to save and proccess data about Point in three dimensional space"""

    def __init__(self, x_var:float, y_var:float, z_var = 0) -> None:
        """ Initialize (x, y) point coordinates"""
        super().__init__(x_var, y_var)
        self.z = z_var

    def __str__(self) -> str:
        """ String representation of self """
        return f'Point in three-dimensional space with coordinates ({self.x}, {self.y}, {self.z})'

    def __repr__(self) -> str:
        """ Represent method """
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other:object) -> bool:
        """ Check if self equels other """
        if not isinstance(other, Point):
            return False
        if not isinstance(other, Point3D):
            return (self.x, self.y, self.z) == (other.x, other.y, 0)
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def vector_length(self) -> float:
        """ Calculate and return vector length """
        return round(sqrt(self.x ** 2 + self.y ** 2 + self.z**2), 2)


def test_classes():
    """ Run tests to check correctness of classes realisation"""
    point1 = Point(17, 2)
    assert (point1.y, point1.x) == (2, 17)
    assert str(point1) == 'Point in two-dimensional space with coordinates (17, 2)'

    point2 = Point3D(17, 4, 2)
    assert (point2.y, point2.z, point2.x) == (4, 2, 17)
    assert str(point2) == "Point in three-dimensional space with coordinates (17, 4, 2)"
    assert str([point1, point2]) == "[Point(x=17, y=2), Point(x=17, y=4, z=2)]"

    assert Point(3, 4) == Point(3, 4)
    assert Point(3, 4) != Point(2, 3)

    assert Point(5, 4) == Point3D(5, 4, 0)
    assert Point3D(5, 4, 0) == Point(5, 4)

    assert Point(5, 4) != Point3D(5, 4, 1)
    assert Point3D(5, 4, 1) != Point(5, 4)

    assert Point3D(8, 7, 0) == Point3D(8, 7)

    assert Point(3, 4).vector_length() == 5
    assert Point(4, 5).vector_length() == 6.4
    assert Point(6, -12).vector_length() == 13.42
    assert Point(100, 0).vector_length() == 100

    assert Point3D(-6, -12, 0).vector_length() == 13.42, Point3D(-6, -12, 0).vector_length()
    assert Point3D(3, 4, 12).vector_length() == 13
    assert Point3D(-13, 14, -15).vector_length() == 24.29


if __name__ == '__main__':
    test_classes()
