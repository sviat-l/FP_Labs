"""
Lab 6.5 Equation
"""

from math import sqrt

class Polynomial:
    """ Polynomial class with basic functionality """

    def __init__(self, coeffs:list) -> None:
        """ Init coeffs list """
        i = 0
        while i < len(coeffs) - 1 and coeffs[i] == 0:
            i += 1
        self.coeffs = list(coeffs[i:]) if coeffs else [0]

    def __eq__(self, other: object) -> bool:
        """ Check if self equels other """
        return self.coeffs == other.coeffs if isinstance(other, Polynomial) else self.degree() == 0 and self.coeff(0) == other

    def degree(self):
        """ Return polynom degree """
        return len(self.coeffs) - 1

    def coeff(self, degree:int):
        """ Return coefficient for the polynom degree """
        return self.coeffs[- degree - 1]

    def evalAt(self, point):
        """ Evaluate and return polynom """
        return sum(point**i * self.coeff(i) for i in range(self.degree()+1))

    def __hash__(self) -> int:
        """ Hash operator """
        return hash(tuple(self.coeffs))

    def scaled(self, scale_number:float):
        """ Return new polynomial with scaled coefficents """
        return Polynomial([scale_number * coeff for coeff in self.coeffs])

    def derivative(self):
        """ Return POlynom that is derivetive of self """
        return Polynomial([i * self.coeff(i) for i in range(self.degree(), 0, -1)])

    def __str__(self) -> str:
        """ String representation of self """
        return f"Polynomial(coeffs={self.coeffs})"

    def addPolynomial(self, other:object):
        """ Create and return new polynom as sum of self and other """
        return Polynomial([ (self.coeff(i) if self.degree() >= i else 0) + (other.coeff(i) if other.degree() >= i else 0) for i in range(max(self.degree(), other.degree()) + 1) ] [::-1]) if isinstance(other, Polynomial) else None

    def multiplyPolynomial(self, other:object):
        """ Create and return new polynom as multiplication of self and other """
        ansver = Polynomial([])
        for i, ind in enumerate(self.coeffs[::-1]):
            ansver = ansver.addPolynomial(Polynomial(other.scaled(ind).coeffs + [0]*i))
        return ansver


class Quadratic(Polynomial):
    """ Class to work with quadratic polynoms """

    def __init__(self, coeffs: list) -> None:
        """ Init class values """
        if len(coeffs) != 3:
            raise ValueError('Invalid coefficient list values')
        super().__init__(coeffs)
        self.a = coeffs[0]
        self.b = coeffs[1]
        self.c = coeffs[2]
        self.D = self.discriminant()

    def __str__(self) -> str:
        """ String representation of self """
        return f'Quadratic(a={self.a}, b={self.b}, c={self.c})'

    def discriminant(self):
        """ Calculate and return discriminatn of the quadratic polynom """
        return self.b**2 - 4 * self.a * self.c

    def numberOfRealRoots(self):
        """ Return number of real roots for quadratic polynom """
        return 0 if self.D < 0 else 1 if self.D == 0 else 2

    def getRealRoots(self):
        """ Return list with quadratic roots """
        return [(-self.b - sqrt(self.D))/(2 * self.a), (-self.b + sqrt(self.D))/(2 * self.a)] if self.numberOfRealRoots() == 2 else [-self.b/(2 * self.a)] if self.numberOfRealRoots()  else []
