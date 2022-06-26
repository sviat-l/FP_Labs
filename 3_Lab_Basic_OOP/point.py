"""
Lab 3.5 Point (Helper Class)
"""

class Point:
    """ Point class for 2-D space """
    def __init__(self, x_var, y_var) -> None:
        """ Init x, y cocords """
        self.x = x_var
        self.y = y_var

    def __repr__(self) -> str:
        """ Representation method """
        return f"{self.__class__.__name__}({self.x}, {self.y})"
