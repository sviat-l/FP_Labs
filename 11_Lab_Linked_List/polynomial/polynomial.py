"""
Polynomial operations with sorted linked list
"""

# Implementation of the Polynomial ADT using a sorted linked list.

class Polynomial:
    """
    Polynomial implemention with linked list
    """
    # Create a new polynomial object.
    def __init__(self, degree = None, coefficient = None):
        if degree is None :
            self._poly_head = None
        else :
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    # Return the degree of the polynomial.
    def degree(self):
        """
        return polynomial degree
        """
        if self._poly_head is None :
            return -1
        else :
            return self._poly_head.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        """
        get item on stated degree
        """
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        cur_node = self._poly_head
        while cur_node is not None and cur_node.degree > degree:
            cur_node = cur_node.next

        if cur_node is None or cur_node.degree != degree:
            return 0.0
        else:
            return cur_node.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        """
        evaluate polynom from scalar representation
        """
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        cur_node = self._poly_head
        while cur_node is not None:
            result += cur_node.coefficient * (scalar ** cur_node.degree)
            cur_node = cur_node.next
        return result

    # Polynomial addition: newPoly = self + rhs_poly.
    def __add__(self, rhs_poly):
        """
        addition of two polynomials
        """
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()

        i = max_degree
        while i >= 0:
            value = self[i] + rhs_poly[i]
            new_poly.append_term(i, value)
            i -= 1
        return new_poly

    # Polynomial subtraction: newPoly = self - rhs_poly.
    def __sub__(self, rhs_poly):
        """
        substraction of two polynomials
        """
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()

        i = max_degree
        while i >= 0:
            value = self[i] - rhs_poly[i]
            new_poly.append_term(i, value)
            i -= 1
        return new_poly

    # Polynomial multiplication: newPoly = self * rhs_poly.
    def __mul__(self, rhs_poly):
        """
        multiplying of two polynomials
        """
        result_poly = None
        current_el = self._poly_head
        # iterate on self polynomial values
        while current_el is not None:
            add_poly = Polynomial()
            other_poly = rhs_poly._poly_head
            while other_poly is not None:
                add_poly.append_term(current_el.degree + other_poly.degree,\
                               current_el.coefficient * other_poly.coefficient)
                other_poly = other_poly.next
            result_poly = add_poly if result_poly is None else result_poly + add_poly
            current_el = current_el.next
        return result_poly

    # Helper method for appending terms to the polynomial.
    def append_term(self, degree, coefficient):
        """
        append value to the polynomial
        """
        if coefficient != 0.0:
            new_term = _PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

    def __str__(self):
        """
        Prints the value stored in self.
        __str__ method
        """
        string = []
        current = self._poly_head
        while current is not None:
            string.append(str(current))
            current = current.next
        return '  '.join(string)


# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return '(' + str(self.coefficient) + " x** " + str(self.degree) + ')'
