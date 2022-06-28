"""
Lab 6.1 Rational
"""

class Rational:
    """ Class with basic operation with Rational numbers """

    def __init__(self, numerator:int, denominator:int) -> None:
        """ Init Rational numenator and denominator """
        self.numenator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        """ String representation of self """
        return f'{self.numenator}/{self.denominator}'

    def __add__(self, other:object):
        """ Adding operator """
        new_num = self.numenator * other.denominator + self.denominator * other.numenator
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __sub__(self, other:object):
        """ Adding operator """
        new_num = self.numenator * other.denominator - self.denominator * other.numenator
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __truediv__(self, other:object):
        """ Adding operator """
        new_num = self.numenator * other.denominator
        new_den = self.denominator * other.numenator
        return Rational(new_num, new_den)

    def __mul__(self, other:object):
        """ Adding operator """
        new_num = self.numenator * other.numenator
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)
