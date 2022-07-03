"""
Middle1 Disc
"""
import math


class Center:
    """
    Class for disc center node
    """
    def __init__(self, x_coord:float, y_coord:float) -> None:
        """
        Init point coords
        """
        self.x = x_coord
        self.y = y_coord

    def __str__(self) -> str:
        """
        String representation of self
        """
        return f'Center is x={self.x}, y={self.y}'


class Disc:
    """
    Main disc class
    """
    def __init__(self, center:Center, radius:int) -> None:
        """
        Init disc parameters
        """
        self.center = (center.x, center.y)
        self.radius = radius

    def __str__(self) -> str:
        """
        String representaion of self
        """
        x_str = f"{'-' if self.center[0] > 0 else '+'}{self.center[0]:.2f}" if self.center[0] else ''
        y_str = f"{'-' if self.center[1] > 0 else '+'}{self.center[1]:.2f}" if self.center[1] else ''
        return "(x"+x_str+')**2 + (y'+y_str+')**2 = '+f'{self.radius**2:.2f}'

    def __hash__(self) -> int:
        """
        Return hash of the disc as
        center coords and radius hash
        """
        return hash((self.center, self.radius))

    def __eq__(self, other: object) -> bool:
        """
        Check if self equels other
        """
        return isinstance(other, Disc) and self.radius == other.radius and self.center == other.center

    @staticmethod
    def distance(point1, point2, presicion:int) -> float:
        """
        Return distance between 2 points with stated presicion
        """
        return round(math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2), presicion)

    def is_touching(self, other:object, precision:int) -> bool:
        """
        Return True if disc self touchs other disc
        with stated precision rate
        """
        dist = self.distance(self.center, other.center, precision)
        return (dist == self.radius + other.radius) or (dist  == abs(self.radius - other.radius))


    def transform_disc(self, change_value:float) -> None:
        """
        Change disc radius on stated value
        """
        self.radius += change_value

    def transformed_disc(self, change_value:float):
        """
        Return new disc changed radius on stated value
        """
        return Disc(Center(*self.center), self.radius + change_value)

    @ staticmethod
    def fromstring(string:str):
        """
        Create and return disc with information from the string
        """
        values = list(map(int, string.split()))
        return Disc(Center(values[0], values[1]), values[2])


    def inscribe_discs(self):
        """
        Return two disc that inscreabe self and have equel radius
        """
        return (Disc(Center((self.center[0] - self.radius/2), (self.center[1])), self.radius/2),
                Disc(Center((self.center[0] + self.radius/2), (self.center[1])), self.radius/2))

    def lens_creation(self, other:object, precision:int):
        """
        It is complicated
        """
        dist = self.distance(self.center, other.center, precision)
        # edge cases: the same center or do not intersect
        if not dist:
            return math.inf
        if dist > self.radius + other.radius:
            return None
        # math calculus
        a = (self.radius**2 - other.radius**2 + dist**2)/(2*dist)
        h = math.sqrt(self.radius**2 - a**2)
        x2 = self.center[0] + a*(other.center[0]-self.center[0])/dist
        y2 = self.center[1] + a*(other.center[1]-self.center[1])/dist
        x3 = round(x2 - h*(other.center[1]-self.center[1])/dist, precision)
        y3 = round(y2 + h*(other.center[0]-self.center[0])/dist, precision)
        x4 = round(x2 + h*(other.center[1]-self.center[1])/dist, precision)
        y4 = round(y2 - h*(other.center[0]-self.center[0])/dist, precision)
        # return 4 points or 1 if self is touching other
        return (self.center, other.center, (x3, y3), (x4, y4)) if \
                        not self.is_touching(other, precision) else (x3, y3)
