"""
Lab 3.5 Triangle
"""

from math import sqrt
import point

class Triangle:
    """ Triangle class. Save points data. Calculate triangle values
    >>> triangle = Triangle(point.Point(6, 0), point.Point(6, 2), point.Point(6, 4))
    >>> triangle.is_triangle()
    False
    >>> triangle = Triangle(point.Point(1, 1), point.Point(3, 1), point.Point(2, 3))
    >>> triangle.is_triangle()
    True
    >>> triangle.perimeter()
    6.47213595499958
    >>> triangle.area()
    2.0
    >>> triangle = Triangle(point.Point(0, 0), point.Point(0, 6), point.Point(8, 0))
    >>> triangle.is_triangle()
    True
    >>> triangle.perimeter()
    24.0
    >>> triangle.area()
    24.0
    """
    def __init__(self, point1:point.Point, point2:point.Point, point3:point.Point) -> None:
        """ Init triangle points """
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def is_triangle(self) -> bool:
        """ Check if 3 points make triangle """
        if self.point2.x == self.point1.x or self.point3.x == self.point1.x:
            return self.point2.x != self.point3.x
        return (self.point3.y- self.point1.y) * (self.point2.x - self.point1.x)\
            != (self.point2.y -self.point1.y) * (self.point3.x -self.point1.x)

    @staticmethod
    def distance(pointA:point.Point, pointB:point.Point) -> float:
        """ Return distance beetween two points"""
        return sqrt((pointB.x - pointA.x)**2 + (pointB.y - pointA.y)**2)

    def perimeter(self) -> float:
        """ Calculate and return triangle's perimeter"""
        return self.distance(self.point1, self.point2)\
                + self.distance(self.point2, self.point3)\
                + self.distance(self.point3, self.point1)

    def area(self) -> float:
        """ Calculate and return self triangle's area """
        return 0.5 * abs(self.point1.x *(self.point2.y - self.point3.y)\
                        + self.point2.x *(self.point3.y - self.point1.y)\
                        + self.point3.x *(self.point1.y - self.point2.y))


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
